# Contributing

Two kinds of contribution are welcome: improvements to the curriculum, and evidence from using it.

## Evidence (most valuable)

- **Bestiary entries.** A failure mode not already in `docs/07-failure-bestiary.md`, with a snippet under ten lines that shows it and the stage where a learner would first meet it. Use the next free ID in the category. Entries with a snippet are merged; entries from theory are discussed first.
- **Stage feedback.** `templates/STAGE_FEEDBACK.md`, filled right after a stage: minutes per rung, stalls, errors you could not read, hidden cases you could not explain. Open it as an issue with the stage-feedback template. It feeds `docs/13-revision-protocol.md`.
- **Cohort data.** Hours per stage, first-attempt gate pass rates, hidden-test counts on first `just eval`, common revise reasons. Anonymised. Open an issue with the data attached; it feeds the table in `docs/11-curriculum-maintenance.md`.
- **Brief bugs.** A rung that cannot be completed on the current pins, an installer screen that no longer matches, a gate that cannot be checked as written, a version number or URL in a brief. Open an issue with the stage and the line.
- **Platform notes.** Anything that differed on your operating system from what the stage 0 or stage 1 brief said.

## Curriculum changes

- **Patch** (pins, typos, reading-list swaps, bestiary additions, a hidden case added with its threshold bump): PR directly. CI must be green: links, board, identifier grep, fixture determinism, `eval.py --solutions --all`.
- **Minor** (a rung, gate wording or convention changes substantively; a stage is rung-numbered): PR with a `CHANGELOG.md` entry and the `REVISIONS.md` entry for each stage touched; for a pin change, the stage 0 reference run on the new pin.
- **Major** (stage structure, thresholds, the topic ladder): open an issue first; then a PR with an ADR in `docs/decisions/` citing cohort data.

## Style

- Terse. Numbers over adjectives. One idea per heading. Worked example before concept.
- Briefs use indirect references ("the installer linked from PINS.md", "the public API"), never versions or URLs. Those go in `PINS.md`.
- At most three new terms per rung; each in the glossary with its stage tag; nothing used before its rung.
- British/Australian spelling. No emojis in briefs.
- Do not add reading-list items; replace them, with a one-line reason.
- Templates may get stricter, not looser.

## Conventional commits

```
docs(s03): split r4 aliasing into r4 (lists) and r4b (nested)
test(s01): add hidden case s01-r4e3-d (empty input); threshold 44/49 -> 45/50
bestiary: add F07 string multiplication by a bool
pins: Python patch bump; stage 0 reference run 2026-xx-xx both platforms
adr: 005 move the debugger rung to stage 3 (with cohort data)
```

## Review

One maintainer approval for patch and minor; two for major. Reviewers apply the same rubric learners face: every claim supported, alternatives considered, a stranger could act on it.
