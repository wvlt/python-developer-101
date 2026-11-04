#!/usr/bin/env python3
"""Build the course fixture: a small, synthetic "neighbourhood library" world.

Deterministic (seeded), standard library only, CC0. Writes to data/library/ by default.

    python data/build_files.py                # writes data/library/*
    python data/build_files.py --seed 7       # a different but equally valid world (held-out set)
    python data/build_files.py --out /tmp/x   # somewhere else (CI determinism check)

Files (schema v1):
    books.csv                   book_id,title,author,year,genre,pages,isbn,copies      (~120 rows)
    members.json                list of {member_id, name, email, suburb, joined}         (~60 members)
    loans.txt                   one loan per line, pipe-separated, deliberately messy    (~400 lines)
    broken/books_latin1.csv     books.csv saved in Latin-1; reading as UTF-8 fails
    broken/books_missing_column.csv   no `pages` column
    broken/members_duplicate_ids.json two members share an id
    broken/loans_bad_dates.txt  three lines with impossible dates
    openlibrary_sample.json     a recorded-shape response for the stage-6 public-API rung
    reference.json              the right answer to every question a brief or hidden test asks of these files

Every exercise or hidden test that reads the fixture checks against reference.json; the answers are computed
here from the same generated data, so the fixture is its own ground truth.
"""
from __future__ import annotations

import argparse
import csv
import json
import random
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

SCHEMA_VERSION = 1
AS_OF = date(2026, 3, 1)  # "today" for every overdue calculation in the course
LOAN_DAYS = 21

FIRST = ("Ada Amara Ana Ben Chen Dana Dev Eli Emma Farah Finn Grace Hana Ivan Jo Kai Lena Luis Maya Milo Nia Noor "
         "Omar Pia Quinn Ravi Rosa Sam Sara Tariq Uma Vik Wren Xin Yara Zane Aiko Bram Cleo Dara Esme Femi Gil Hugo "
         "Ines Jun Kofi Leila").split()
LAST = ("Okafor Lindqvist Haddad Moreau Tanaka Novak Silva Brennan Iyer Kowalski Mensah Petrov Rahman Schmidt Torres "
        "Varga Walsh Yilmaz Zhou Abara Bakker Costa Dubois Eriksen Fischer Garcia Hassan Ibarra Jensen Karim Larsen "
        "Nakamura Osei Quist").split()
SUBURBS = ["Northcote", "Fitzroy", "Brunswick", "Coburg", "Preston", "Thornbury", "Carlton", "Kensington"]
GENRES = ["fiction", "mystery", "science", "history", "poetry", "children", "cooking", "travel"]
ADJ = ("Quiet Salt Winter Paper Hollow Long Last Small Blue Iron Glass Borrowed Early Distant Green Silent Red Open "
       "Broken Northern").split()
NOUN = ("Harbour River Garden Lantern Orchard Map Letter Bridge Kitchen Island House Field Window Road Market Tide "
        "Bell Forest Clock Shore").split()
PATTERNS = ["The {a} {n}", "{a} {n}s", "A {n} of {a2} {n2}s", "{n} and {n2}", "The {n} at {a} {n2}", "{a} {n}, {a2} {n2}"]


def rand_name(r: random.Random) -> str:
    return f"{r.choice(FIRST)} {r.choice(LAST)}"


def rand_title(r: random.Random) -> str:
    p = r.choice(PATTERNS)
    return p.format(a=r.choice(ADJ), a2=r.choice(ADJ), n=r.choice(NOUN), n2=r.choice(NOUN))


def isbn13(r: random.Random) -> str:
    digits = [9, 7, 8] + [r.randint(0, 9) for _ in range(9)]
    check = (10 - sum(d * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits)) % 10) % 10
    return "".join(map(str, digits + [check]))


def build(seed: int) -> dict:
    r = random.Random(seed)

    # ---- books -------------------------------------------------------------
    books: list[dict] = []
    seen_titles: set[str] = set()
    authors = [rand_name(r) for _ in range(40)]
    while len(books) < 120:
        title = rand_title(r)
        if title in seen_titles:
            continue
        seen_titles.add(title)
        books.append({
            "book_id": f"B{len(books) + 1:03d}",
            "title": title,
            "author": r.choice(authors),
            "year": r.randint(1948, 2025),
            "genre": r.choice(GENRES),
            "pages": r.randint(60, 720),
            "isbn": isbn13(r),
            "copies": r.choice([1, 1, 1, 2, 2, 3]),
        })

    # ---- members -----------------------------------------------------------
    members: list[dict] = []
    seen_names: set[str] = set()
    while len(members) < 60:
        name = rand_name(r)
        if name in seen_names:
            continue
        seen_names.add(name)
        joined = date(2022, 1, 1) + timedelta(days=r.randint(0, 1400))
        first, last = name.split()
        members.append({
            "member_id": f"M{len(members) + 1:03d}",
            "name": name,
            "email": f"{first.lower()}.{last.lower()}@example.com",
            "suburb": r.choice(SUBURBS),
            "joined": joined.isoformat(),
        })

    # ---- loans (clean records first; mess added when written) --------------
    loans: list[dict] = []
    heavy = r.sample([m["member_id"] for m in members], 6)  # a few members borrow a lot
    popular = r.sample([b["book_id"] for b in books], 8)
    for i in range(400):
        mid = r.choice(heavy) if r.random() < 0.35 else r.choice(members)["member_id"]
        bid = r.choice(popular) if r.random() < 0.3 else r.choice(books)["book_id"]
        out = date(2025, 6, 1) + timedelta(days=r.randint(0, 270))
        due = out + timedelta(days=LOAN_DAYS)
        roll = r.random()
        if roll < 0.78:
            returned: date | None = out + timedelta(days=r.randint(2, 35))
        else:
            returned = None
        if returned and returned > AS_OF:
            returned = None
        if returned:
            status = "returned"
        elif due < AS_OF:
            status = "overdue"
        else:
            status = "out"
        loans.append({"loan_id": f"L{i + 1:04d}", "member_id": mid, "book_id": bid, "out": out.isoformat(),
                      "due": due.isoformat(), "returned": returned.isoformat() if returned else "", "status": status})

    return {"books": books, "members": members, "loans": loans, "rng": r}


def messy_loan_line(r: random.Random, ln: dict) -> str:
    fields = [ln["loan_id"], ln["member_id"], ln["book_id"], ln["out"], ln["due"], ln["returned"], ln["status"]]
    roll = r.random()
    if roll < 0.15:
        fields = [f" {f} " if r.random() < 0.5 else f for f in fields]       # stray spaces
    if roll < 0.10:
        fields[6] = fields[6].upper()                                        # STATUS in capitals
    elif roll < 0.18:
        fields[6] = fields[6].capitalize()
    return "|".join(fields)


def reference(world: dict) -> dict:
    books, members, loans = world["books"], world["members"], world["loans"]
    by_genre = Counter(b["genre"] for b in books)
    by_suburb = Counter(m["suburb"] for m in members)
    loans_per_member = Counter(ln["member_id"] for ln in loans)
    loans_per_book = Counter(ln["book_id"] for ln in loans)
    oldest = min(books, key=lambda b: (b["year"], b["book_id"]))
    longest_title = max(books, key=lambda b: (len(b["title"]), b["book_id"]))
    thickest = max(books, key=lambda b: (b["pages"], b["book_id"]))
    overdue = [ln for ln in loans if ln["status"] == "overdue"]
    returned = [ln for ln in loans if ln["returned"]]
    late_returns = [ln for ln in returned if ln["returned"] > ln["due"]]
    days_out = [(date.fromisoformat(ln["returned"]) - date.fromisoformat(ln["out"])).days for ln in returned]
    top_member = loans_per_member.most_common(1)[0]
    top_book = loans_per_book.most_common(1)[0]
    members_by_id = {m["member_id"]: m for m in members}
    books_by_id = {b["book_id"]: b for b in books}
    copies_out = Counter(ln["book_id"] for ln in loans if ln["status"] != "returned")
    over_lent = sorted(bid for bid, n in copies_out.items() if n > books_by_id[bid]["copies"])
    return {
        "schema_version": SCHEMA_VERSION,
        "as_of": AS_OF.isoformat(),
        "loan_days": LOAN_DAYS,
        "q01_book_count": len(books),
        "q02_member_count": len(members),
        "q03_loan_count": len(loans),
        "q04_books_per_genre": dict(sorted(by_genre.items())),
        "q05_members_per_suburb": dict(sorted(by_suburb.items())),
        "q06_oldest_book": {"book_id": oldest["book_id"], "title": oldest["title"], "year": oldest["year"]},
        "q07_longest_title": {"book_id": longest_title["book_id"], "title": longest_title["title"],
                              "length": len(longest_title["title"])},
        "q08_total_pages": sum(b["pages"] for b in books),
        "q09_mean_pages": round(sum(b["pages"] for b in books) / len(books), 2),
        "q10_thickest_book": {"book_id": thickest["book_id"], "pages": thickest["pages"]},
        "q11_distinct_authors": len({b["author"] for b in books}),
        "q12_total_copies": sum(b["copies"] for b in books),
        "q13_overdue_count": len(overdue),
        "q14_overdue_loan_ids": sorted(ln["loan_id"] for ln in overdue),
        "q15_status_counts": dict(sorted(Counter(ln["status"] for ln in loans).items())),
        "q16_top_member": {"member_id": top_member[0], "name": members_by_id[top_member[0]]["name"], "loans": top_member[1]},
        "q17_top_book": {"book_id": top_book[0], "title": books_by_id[top_book[0]]["title"], "loans": top_book[1]},
        "q18_members_with_no_loans": sorted(m["member_id"] for m in members if m["member_id"] not in loans_per_member),
        "q19_books_never_borrowed": sorted(b["book_id"] for b in books if b["book_id"] not in loans_per_book),
        "q20_late_return_count": len(late_returns),
        "q21_mean_days_out": round(sum(days_out) / len(days_out), 2),
        "q22_max_days_out": max(days_out),
        "q23_over_lent_books": over_lent,
        "q24_titles_sorted_first_five": [b["title"] for b in sorted(books, key=lambda b: b["title"])[:5]],
        "q25_books_by_year_then_title_first_five": [b["book_id"] for b in sorted(books, key=lambda b: (b["year"], b["title"]))[:5]],
        "q26_authors_with_most_books": sorted(a for a, n in Counter(b["author"] for b in books).items()
                                              if n == max(Counter(b["author"] for b in books).values())),
        "q27_members_joined_2024": sum(1 for m in members if m["joined"].startswith("2024")),
        "q28_email_domains": sorted({m["email"].split("@")[1] for m in members}),
        "q29_loans_by_month": dict(sorted(Counter(ln["out"][:7] for ln in loans).items())),
        "q30_suburb_with_most_members": max(sorted(by_suburb), key=lambda s: by_suburb[s]),
        "broken": {
            "members_duplicate_ids": ["M007"],
            "books_missing_column": "pages",
            "books_latin1_author_with_accent": "Inés Moreau",
            "loans_bad_dates_line_numbers": [3, 17, 25],
        },
    }


def write(world: dict, out: Path) -> None:
    r: random.Random = world["rng"]
    out.mkdir(parents=True, exist_ok=True)
    (out / "broken").mkdir(exist_ok=True)
    books, members, loans = world["books"], world["members"], world["loans"]

    with (out / "books.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(books[0].keys()))
        w.writeheader()
        w.writerows(books)

    (out / "members.json").write_text(json.dumps(members, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = ["# neighbourhood library — loans export. one loan per line: loan_id|member_id|book_id|out|due|returned|status", ""]
    for i, ln in enumerate(loans):
        lines.append(messy_loan_line(r, ln))
        if i % 97 == 50:
            lines.append("")  # stray blank lines
    (out / "loans.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # broken: latin-1 encoded copy with an accented author
    latin_books = [dict(b) for b in books]
    latin_books[4]["author"] = "Inés Moreau"
    with (out / "broken" / "books_latin1.csv").open("w", newline="", encoding="latin-1") as f:
        w = csv.DictWriter(f, fieldnames=list(books[0].keys()))
        w.writeheader()
        w.writerows(latin_books)

    # broken: missing column
    with (out / "broken" / "books_missing_column.csv").open("w", newline="", encoding="utf-8") as f:
        cols = [c for c in books[0].keys() if c != "pages"]
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(books)

    # broken: duplicate member id
    dup = [dict(m) for m in members]
    dup[20]["member_id"] = "M007"
    (out / "broken" / "members_duplicate_ids.json").write_text(json.dumps(dup, indent=2, ensure_ascii=False) + "\n",
                                                              encoding="utf-8")

    # broken: bad dates on lines 3, 17, 25 (1-based, counting the two header lines)
    bad = lines[:40]
    for n, fake in ((3, "2026-13-40"), (17, "2025-02-30"), (25, "26/01/2026")):
        parts = bad[n - 1].split("|")
        if len(parts) == 7:
            parts[3] = fake
            bad[n - 1] = "|".join(parts)
    (out / "broken" / "loans_bad_dates.txt").write_text("\n".join(bad) + "\n", encoding="utf-8")

    # a recorded-shape public API response (shape of the Open Library search endpoint, synthetic content)
    sample = {
        "numFound": 3, "start": 0, "numFoundExact": True,
        "docs": [
            {"title": books[0]["title"], "author_name": [books[0]["author"]], "first_publish_year": books[0]["year"]},
            {"title": books[1]["title"], "author_name": [books[1]["author"]], "first_publish_year": books[1]["year"]},
            {"title": books[2]["title"], "author_name": [books[2]["author"], books[3]["author"]],
             "first_publish_year": books[2]["year"]},
        ],
        "q": books[0]["title"].lower(),
    }
    (out / "openlibrary_sample.json").write_text(json.dumps(sample, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    (out / "reference.json").write_text(json.dumps(reference(world), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", type=Path, default=Path(__file__).resolve().parent / "library")
    a = ap.parse_args()
    world = build(a.seed)
    write(world, a.out)
    ref = json.loads((a.out / "reference.json").read_text(encoding="utf-8"))
    print(f"wrote {a.out}: {ref['q01_book_count']} books, {ref['q02_member_count']} members, "
          f"{ref['q03_loan_count']} loans ({ref['q13_overdue_count']} overdue as of {ref['as_of']}), seed {a.seed}")


if __name__ == "__main__":
    main()
