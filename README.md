# Python Developer 101

**From "I have never written a line of code" to "I can be dropped into an engineering team and be useful in week one."**

This repository is a complete, evidence-based curriculum for learning Python as a professional would use it. It is ten stages long, each stage ends in a working program with tests and a measurable gate, and the whole thing is designed around one conviction: the scarce skill is not knowing the syntax, it is **fluency with judgment** — writing idiomatic Python without thinking, reading the error when it fails, seeing inside it when it is quietly wrong, and knowing when not to write code at all.

<!-- board:start -->
<!-- board:end -->

## Who this is for

You have never programmed. You can install an application, use a browser and a spreadsheet, and manage files and folders. You have never opened a terminal, never used git, and do not know what a variable, a loop, a file path or a package is. That is the only assumed starting point, and every one of those words is on the ladder. Detail in [`CONTEXT.md`](CONTEXT.md).

## The ladder at a glance

Four tiers, ten gated stages plus a two-hour on-ramp, four strands in every stage (**Build**, **Measure**, **Break**, **Inspect**).

**Tier A — Talking to the machine**
0. [Hello, Python](stages/00-hello-python/) — install, open a terminal, `print("Hello, world")`, break it on purpose, read the error
1. [Values and names](stages/01-values-and-names/) — numbers, strings, variables, f-strings; `uv`, your first tests, git as save points
2. [Decisions and repetition](stages/02-decisions-and-repetition/) — `if`, `match`, `while`, `for`, `range`, `zip`; a text game; GitHub and `ruff`
3. [Collections](stages/03-collections/) — lists, tuples, dicts, sets, comprehensions, `sorted`, `lambda`; aliasing, the first quiet bug

**Tier B — Structure**
4. [Functions](stages/04-functions/) — `def`, scope, defaults, `*args`, closures, a decorator, recursion; the debugger
5. [Errors, files and the outside world](stages/05-errors-and-files/) — exceptions, `with`, `pathlib`, CSV, JSON, `pickle`, `argparse`, `logging`
6. [Modules, packages and tooling](stages/06-modules-and-tooling/) — `import`, packages, the standard-library tour, `uv add`, your first own tests

**Tier C — Objects**
7. [Classes and objects](stages/07-classes-and-objects/) — `class`, `self`, `__repr__`, properties, dataclasses, `Enum`; the library world as classes
8. [Design and the data model](stages/08-design-and-the-data-model/) — inheritance, composition, protocols, dunders, iterators, generators, context managers

**Tier D — Craft**
9. [Writing Python well](stages/09-writing-python-well/) — idioms, typing with `mypy`, testing in depth, performance, refactoring, reading code
10. [Capstone](stages/10-capstone/) — a tested, typed, documented command-line application; a peer breaks it; you teach one concept back

About 140 hours; roughly 15 weeks at 8–10 hours per week. Full detail in the [syllabus](docs/01-syllabus.md).

## Start here

0. Read [`CONTEXT.md`](CONTEXT.md) — who this is for, where it ends, and how the curriculum changes in response to you.
1. Read [`docs/00-intent.md`](docs/00-intent.md) — ten minutes, and it explains every design decision that follows.
2. Open [`stages/00-hello-python/README.md`](stages/00-hello-python/README.md). Two hours, no gate, no accounts, no cost. It installs everything you need and ends with a program you wrote running from the terminal.
3. Then read [`docs/02-getting-started.md`](docs/02-getting-started.md) — how to work a stage, how tests and the eval harness work, and the AI-assistance policy.

## Documentation map

| Document | What it is |
|---|---|
| [00 — Intent](docs/00-intent.md) | Why this exists, what mastery means, what we deliberately leave out, the Programmer's Oath |
| [01 — Syllabus](docs/01-syllabus.md) | All ten stages: objectives, strands, break-labs, artefacts, gates, time budget |
| [02 — Getting started](docs/02-getting-started.md) | Tooling ramp, how to work a stage, tests and `just eval`, solutions policy, AI-assistance policy |
| [03 — Pedagogy](docs/03-pedagogy.md) | The evidence base and how each finding became a design rule |
| [04 — Platform and tooling](docs/04-platform-and-tooling.md) | Local-first and free; the toolchain and why each piece |
| [05 — Conventions](docs/05-conventions.md) | Repo layout, naming, IDs, exercises and tests as files, commits |
| [06 — Assessment and gates](docs/06-assessment-and-gates.md) | The eval harness, thresholds, the universal checklist, what "passing a stage" means |
| [07 — Failure bestiary](docs/07-failure-bestiary.md) | How Python programs fail, loudly and quietly: symptom, cause, detection, fix, stage, ID |
| [08 — Glossary](docs/08-glossary.md) | Every term the course uses, defined once, with the stage that introduces it |
| [09 — Reading list](docs/09-reading-list.md) | Primary sources per stage, with why each one matters |
| [10 — Instructor guide](docs/10-instructor-guide.md) | Running a cohort: pacing, misconceptions, the "break my program" protocol, grading |
| [11 — Curriculum maintenance](docs/11-curriculum-maintenance.md) | How this repo stays current |
| [12 — Capability map](docs/12-capability-map.md) | Every destination capability and every ladder topic traced to the rung that delivers it |
| [13 — Revision protocol](docs/13-revision-protocol.md) | Rung changes vs contract changes vs stage changes; the cascade check |
| [14 — Rubrics](docs/14-rubrics.md) | Rung rubric (Run · See · Say), stage rubric (six dimensions, three levels), gate IDs, the 20-minute review |
| [15 — Authoring guide](docs/15-authoring-guide.md) | Content model, brief structure, voice, code and exercise rules, definition of done |
| [16 — Build readiness](docs/16-build-readiness.md) | Pre-flight list before materials for a stage are authored |
| [17 — Focus map](docs/17-focus-map.md) | Per stage: concept lane, tooling lane, data lane, and what is deliberately deferred |
| [PINS.md](PINS.md) | The pinned versions, install links and fixtures every brief refers to by role |
| [BOARD.md](BOARD.md) | Course outline with your progress per stage and rung; maintainer view folded underneath |
| [Course player](https://wvlt.github.io/python-developer-101/) | The same, as a page: stages, parts and rungs on the left, the brief on the right (`just site` runs it locally) |
| [Templates](templates/) | Artefact card, ADR, error analysis, failure review, break-my-program report, post-mortem, journal, stage feedback, gate review, progress log, rung |

## How this curriculum changes

Stages are stable: outcome, gate, and a **contract** (what each stage assumes and provides). Rungs inside stages — with IDs like `s02-r4b` — change freely in response to learner feedback, and each stage keeps a `REVISIONS.md` log. When a learner stalls, the answer is a new rung, not a new stage. Feedback starts at stage 0 and cascades forward along the contracts. Details in [`CONTEXT.md`](CONTEXT.md) and [docs/13](docs/13-revision-protocol.md).

## Principles in one breath

Run it before you say it works. Read the whole error before you change anything. Do not trust a test you have never seen fail. Never ship a program you cannot see inside. Standard library before a package, and no code at all before either. And sometimes the right program is a spreadsheet.

## Licence

Code is MIT. Written course material is CC BY 4.0. Synthetic fixtures are CC0. See [LICENSE](LICENSE).

Built by [AI Tech Institute](https://www.aitechinstitute.com.au/) — *Production-grade, not notebooks.*
