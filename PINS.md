# PINS.md — pinned volatile choices

The single place where fast-changing identifiers live: versions, download links, the public API, the fixture. Briefs refer to roles ("the Python version", "the editor", "the public API named in PINS.md"); this file says what those are *for the current cohort*. CI (`scripts/check_pins.py`) fails if a version number or download URL appears in a brief or doc. Updated at every cohort start and on any deprecation notice, per [11 — Curriculum maintenance](docs/11-curriculum-maintenance.md). A pin change is a PR that includes a re-run of the stage-0 reference run and `just eval --solutions --all`.

**Cohort:** first (owner as learner)
**Curriculum version:** v1.0.0
**Pinned on:** 2026-11-04. Sources: python.org downloads and release pages; endoflife.date/python; pypi.org JSON API for each package; the VS Code Marketplace page for the Python extension; GitHub Releases for VS Code, Git for Windows, gitleaks, just, ruff-pre-commit and pre-commit-hooks; docs.astral.sh/uv installation page; openlibrary.org search endpoint, queried live.

**There is no model, no cloud and no paid tool anywhere in this course.** The only account the learner creates is a free GitHub account, at stage 2. The ledger tracks hours, not money.

## How to re-pin (maintainers, each cohort)

1. **Python.** Open python.org/downloads. Record the latest release *in the pinned minor* that ships binary installers for Windows and macOS (a minor that has entered security-only support publishes source-only releases; the installer link must point at the last binary release). Decide whether to move the minor: the course uses nothing newer than `match`/`case` and `X | Y` unions (3.10), so any supported minor works; parity with the sibling courses decides. Record the exact installer version and the two download links.
2. **Editor.** Record the current VS Code version from its GitHub releases and the current Python extension version from the Marketplace page. Confirm the Python extension still bundles the debugger extension (it has since 2023).
3. **uv.** `curl -s https://pypi.org/pypi/uv/json`; record the version and confirm the two install commands on the installation page are unchanged.
4. **Packages.** Same PyPI query for pytest, ruff, mypy, pytest-cov, requests, rich, pre-commit. Record versions and `requires_python`. Update `pyproject.toml` lower bounds to the pinned minor (not the patch) and `.pre-commit-config.yaml` revs to the exact tags.
5. **Git.** Record the Git for Windows release; macOS uses the Xcode command-line tools' git (version is whatever Apple ships; ≥ 2.39 is fine).
6. **Public API.** `curl` the search endpoint with the query used in the stage-6 brief and confirm it returns JSON with the fields the brief reads (`title`, `author_name`, `first_publish_year`). If it does not, choose another no-key JSON API and update the role row and the stage-6 exercise data.
7. Run stage 0 end to end on a clean user account on both platforms if possible; run `python scripts/eval.py --solutions --all`; record both in the deprecation log.

## Runtime and editor

| Role | Choice | Exact pin | Install | Caveats | Used from |
|---|---|---|---|---|---|
| **Python** | CPython 3.13 | **3.13.17** (released 2026-10-21; last 3.13 release with binary installers) | Windows: https://www.python.org/ftp/python/3.13.17/python-3.13.17-amd64.exe · macOS: https://www.python.org/ftp/python/3.13.17/python-3.13.17-macos11.pkg · release page https://www.python.org/downloads/release/python-31317/ | 3.13 entered **security-only** support in October 2026 (3.13.18, 2026-10-25, is source-only; end of life 2029-10). Pinned for parity with the sibling courses, which assume 3.13 on entry; nothing the course teaches differs between 3.13 and 3.15. The Windows installer must be run with **"Add python.exe to PATH" ticked**. On macOS the command is `python3`; the installer does not create `python`. From stage 1, `uv` manages Python (`uv python install 3.13` fetches 3.13.18) and the command becomes `uv run python` on both platforms. | s00-r0 |
| **Editor** | Visual Studio Code | **1.144.0** (2026-10-28) | https://code.visualstudio.com/download | Free, no account. Install the **Python** extension (below) from the Extensions pane; nothing else. Turn off AI completions in the editor for stages 0–6 (docs/02, AI-assistance policy). | s00-r0 |
| **Editor Python extension** | ms-python.python | **2026.11.2026102901** (2026-10-29) | https://marketplace.visualstudio.com/items?itemName=ms-python.python | Bundles the Python Debugger extension (ms-python.debugpy), used at s04. | s00-r0 (install), s04 (debugger) |
| **Terminal** | Windows: Windows Terminal or PowerShell · macOS: Terminal.app | ships with the OS | — | Stage 0 names both and shows how to open each. Linux learners follow the macOS column. | s00-r1 |

## Toolchain

| Role | Choice | Exact pin | Install | Caveats | Used from |
|---|---|---|---|---|---|
| **Package and project manager** | uv | **0.13.7** (2026-11-03) | macOS: `curl -LsSf https://astral.sh/uv/install.sh \| sh` · Windows (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"` · docs https://docs.astral.sh/uv/getting-started/installation/ | One tool for Python versions, virtual environments, dependencies and running scripts; replaces `pip`, `venv` and `pyenv` for this course. The learner never types `pip install`. | s01-r0 |
| **Command runner** | just | **1.59.0** (2026-10-15) | `uv tool install rust-just` (PyPI package `rust-just` 1.59.0) | Gives `just test`, `just eval`, `just break`, `just board`, `just site`. The `justfile` is the only Makefile-like thing in the course. | s01-r0 |
| **Version control** | git | Windows: **Git for Windows 2.56.0** (2026-10-26) https://git-scm.com/download/win · macOS: Xcode command-line tools (`xcode-select --install`) | | Stage 1 teaches `init`/`status`/`add`/`commit`/`log` only ("save points"). Branches and pull requests arrive at stage 2 with GitHub. | s01-r8 |
| **Hosting** | GitHub (free) | — | https://github.com/signup | The only account in the course. Fork, push, Pages for your own course player. Two-factor setup is part of the rung. | s02-r10 |
| **Test runner** | pytest | **9.2.0** (2026-10-27) | via `uv sync` (dev group) | Run by the learner from s01; written by the learner from s06. | s01-r0 |
| **Linter and formatter** | ruff | **0.17.3** (2026-10-27) | via `uv sync` (dev group); pre-commit rev `v0.17.3` | `ruff check` at s02; `ruff format` at s09. Rule set in `pyproject.toml`. | s02-r9 |
| **Type checker** | mypy | **2.4.1** (2026-10-28) | via `uv sync` (dev group) | Type hints are written from s04 and checked from s09. | s09 |
| **Coverage** | pytest-cov | **7.1.0** (2026-03-21) | via `uv sync` (dev group) | ≥ 90 % on the capstone. | s09 |
| **Pre-commit** | pre-commit | **4.7.0** (2026-10-12); hooks: ruff-pre-commit `v0.17.3`, gitleaks `v8.30.1`, pre-commit-hooks `v6.0.0` | via `uv sync` (dev group); `uv run pre-commit install` | Optional for learners before s09; required for maintainers. | s09 (learner) |

## Third-party packages the course touches

| Role | Choice | Exact pin | Why this one | Used from |
|---|---|---|---|---|
| **HTTP client** | requests | **2.34.2** (2026-05-14) | The most-read HTTP library in existing Python code; a junior will meet it in week one. The standard library's `urllib.request` is shown first so the learner sees what `requests` saves them. | s06 |
| **Terminal output** | rich | **15.0.0** (2026-04-12) | Tables and colour for the stage-6 and capstone command-line programs; demonstrates `uv add` and reading a package's documentation. Optional in the capstone. | s06 |

No other third-party package appears in a brief. `pydantic`, web frameworks, data-science libraries and notebooks are out of scope (docs/00).

## Public API

| Role | Choice | Endpoint | Licence / terms | Used from |
|---|---|---|---|---|
| **The public API** | Open Library Search API | `https://openlibrary.org/search.json?q=<query>&limit=<n>&fields=title,author_name,first_publish_year` — docs https://openlibrary.org/dev/docs/api/search | No key. Data CC0 / public domain; API asks for a descriptive `User-Agent`. Verified 2026-11-04: `q=the+hobbit&limit=2` returned `numFound: 461` and two documents with the three fields. | s06 |

Chosen because it fits the library-world fixture, needs no account, and returns small JSON. If it is unavailable on the day, the stage-6 brief says to use the recorded response in `data/library/openlibrary_sample.json` (written by the fixture generator) and note it in the journal.

## Fixtures

| Fixture | Source | Version | Licence |
|---|---|---|---|
| The neighbourhood library world — `data/library/` (`books.csv`, `members.json`, `loans.txt`, `broken/*`, `reference.json`, `openlibrary_sample.json`) | `python data/build_files.py` (purpose-built, seeded, standard library only) | schema v1, seed 42 | CC0 (synthetic; names from short word lists; no real people, no real books) |

Used from stage 3; the capstone persists to it. No external dataset anywhere in the course.

## Reference runs

The exact interpreter each stage's code blocks were last executed on. Briefs and `REVISIONS.md` refer to this table rather than naming a patch version.

| Date | Stage | Platform | Interpreter | Pin at the time | Result |
|---|---|---|---|---|---|
| 2026-11-04 | s00 | macOS 15, Apple silicon | CPython **3.13.1** (system package manager; the pinned installer was not run on the maintainer's machine) | 3.13.17 | 22 blocks; 19 matched, 3 brief changes (`stages/00-hello-python/REVISIONS.md`). Error messages and `print`/`input` behaviour are identical across 3.13 patch releases; re-run on the pinned installer and on Windows before the first Windows learner. |
| 2026-11-04 | s01, s02 | macOS 15 | CPython **3.13.1** | 3.13.17 | Prompt examples evaluated and visible-test counts confirmed (`REVISIONS.md` of each stage); full by-hand run pending at stage verification. |

## Deprecation log

| Date | What changed | Why | Reference run before → after |
|---|---|---|---|
| 2026-11-04 | Initial pins | Course created | stage-0 reference run in `stages/00-hello-python/REVISIONS.md` |
