# 03 — Pedagogy

This document records the evidence behind the curriculum's shape, so that future maintainers change the design for reasons rather than taste. Each finding is paired with the design rule it produced and where that rule shows up. The learner here is an absolute beginner, and several findings bite harder for that reason; those are marked.

## Findings and the rules they produced

### Worked-example effect and cognitive load — Sweller (1988 onward); Sweller, van Merriënboer & Paas (2019 review)

**Finding:** Novices learn more from studying worked examples than from solving equivalent problems, because unguided problem-solving overloads working memory. The effect reverses for experts (expertise reversal), who learn more from problem-solving. *This is the single most important finding for this learner.*

**Rule:** Every rung is a **worked example first**: complete code, typed, run, seen — then exercises that vary one thing. Tier A shows every line; Tier B shows every function; Tier C shows the shape of a class and asks for the rest; Tier D gives constraints. Vocabulary is capped at three new terms per rung. No concept appears in code before it is introduced.

**Where:** the structure of every rung; the vocabulary cap in CONTEXT.md and the definition of done in docs/15; the fade from stage 0's full scripts to stage 9's constraints.

### Productive failure — Kapur (2008, 2016)

**Finding:** Students who first attempt problems they cannot yet solve, *then* receive instruction, outperform students who receive instruction first — particularly on conceptual understanding and transfer. The struggle activates prior knowledge and makes the subsequent explanation land.

**Rule:** Every stage opens with a break-lab the learner performs before reading the Build section: **predict the output, then run it**, on six to ten snippets chosen to expose the stage's misconceptions, plus a planted bug to find. Stage 0's "make it fail on purpose" is the same finding at the smallest scale: the learner meets `NameError` and `SyntaxError` deliberately before meeting them by accident.

**Where:** Break-lab sections in every stage; `breaklab/` directories; `just break`.

### Mastery learning — Bloom (1984), "The 2 Sigma Problem"

**Finding:** Students taught under mastery conditions (do not advance until the current unit is demonstrably learned, with corrective feedback) perform about one standard deviation above conventional instruction.

**Rule:** Every stage has a measurable gate — ≥ N of M hidden tests plus the Say questions — and you do not advance without passing it. Gates are criteria, not deadlines. The hidden set exists so that "learned" means "can do it on an input you have not seen", not "made the visible tests green".

**Where:** Gate sections; `just eval`; [06 — Assessment](06-assessment-and-gates.md).

### Testing effect and retrieval practice — Roediger & Karpicke (2006); Karpicke & Blunt (2011)

**Finding:** Retrieving knowledge from memory strengthens it far more than re-reading; the effect is large and durable.

**Rule:** Every rung ends with **Say**: one sentence the learner must produce without notes. Every gate asks three Say questions from earlier rungs. The stage-10 teach-back is retrieval at scale. The exercise volume (four to eight per rung, ~250 across the course) is retrieval practice in code: each one asks the learner to produce, from memory, the construct the worked example showed.

**Where:** the Check block of every rung; gate Say items; the teach-back.

### Spacing and interleaving — Cepeda et al. (2006); Rohrer & Taylor (2007)

**Finding:** Practice spread over time and mixed across topics produces more durable learning than massed practice on one topic, even though massed practice feels more productive.

**Rule:** The four strands spiral: tracebacks are read in every stage, not in a "debugging" week; tests are run from stage 1 and written from stage 6; the library world returns in every stage from 3 with a new question. Each stage's mini-project deliberately uses the previous two stages' constructs. Hidden tests include cases from earlier stages' concepts.

**Where:** the strand structure; the mini-project rungs; the data lane in docs/17.

### Deliberate practice — Ericsson, Krampe & Tesch-Römer (1993)

**Finding:** Expertise comes from practice that is effortful, targeted at specific weaknesses, and accompanied by immediate, informative feedback. Time on task alone predicts little.

**Rule:** Feedback is immediate and specific: a failing test prints the input, the expected output and yours, side by side, in under a second. The eval harness names the exercise and the case. Stall notes in `PROGRESS.md` target the maintainer's next rung at the learner's actual weakness.

**Where:** `course/runner.py`'s error messages; `just eval`'s table; the feedback flow in CONTEXT.md.

### Notional machine and misconceptions in novice programming — du Boulay (1986); Sorva (2013); Qian & Lehman (2017 review)

**Finding:** Novice programmers' errors cluster around a small set of stable misconceptions about how the machine executes code: that a variable is a box with a name written on it rather than a name pointing at a value; that assignment is an equation; that the computer understands intent; that a loop variable "knows" its purpose; that `if` is checked continuously. Explicit teaching of the *notional machine* — a simplified, correct model of execution — reduces these.

**Rule:** The course's first mental model, installed in Tier A, is **the computer does exactly what you wrote**. Names-point-at-objects is taught with `id()` and a drawing at stage 3 before functions complicate it. `just trace` shows execution line by line so the learner sees the machine rather than imagining it. The bestiary catalogues the misconceptions by ID.

**Where:** the Tier A framing; `course/tracer.py`; the aliasing rungs in stage 3; [07 — Failure bestiary](07-failure-bestiary.md).

### Reading error messages — Becker et al. (2019 review); Marceau, Fisler & Krishnamurthi (2011)

**Finding:** Novices routinely do not read error messages, or read only the first line, and the messages' vocabulary is a barrier. Explicit instruction in reading them, and messages written for novices, measurably reduce time to fix.

**Rule:** Stage 0 rung 5 is *make it fail on purpose and read each error slowly*; the brief walks through the message word by word. Every stage's break-lab includes a traceback to read bottom-up. The test runner's messages avoid jargon and say what to do next. Python 3.13's own improved messages ("Did you mean…?") are pointed at explicitly.

**Where:** s00-r5; `course/runner.py`; the traceback rungs in s01, s04, s05.

### Self-explanation — Chi et al. (1989)

**Finding:** Students who explain worked examples to themselves while studying learn more than those who do not, and the effect is large.

**Rule:** The journal is mandatory. The Say item of every Check is a forced self-explanation. The Artefact Card forces explanation of every design decision from stage 4.

**Where:** `JOURNAL.md`, the Check blocks, `ARTIFACT_CARD.md`.

### Working-memory capacity — Miller (1956), Cowan (2001)

**Finding:** People hold roughly four chunks in working memory at once.

**Rule:** Four tiers, four strands, at most three new terms per rung, code blocks under 25 lines in Tier A.

**Where:** Tier structure; the vocabulary cap; the code rules in docs/15.

### Spiral curriculum — Bruner (1960)

**Finding:** Complex ideas are best taught early in simplified form and revisited repeatedly at increasing depth.

**Rule:** `lambda` appears with `sorted(key=…)` at stage 3 and is deepened at stage 4. Context managers are used at stage 5 and written at stage 8. Exceptions are caught at stage 5 and designed at stage 8. Tests are run at stage 1, written at stage 6, measured at stage 9.

**Where:** the ★ topics in the syllabus; the capability map's "deepened" column.

### Transfer and underlying structure — Bransford, Brown & Cocking (2000), *How People Learn*

**Finding:** Transfer to new contexts depends on understanding the underlying principles, not surface features.

**Rule:** Standard library before packages; `urllib` before `requests`; a hand-written `Counter` before `collections.Counter`; your own `__iter__` before relying on generators. The learner sees what the convenience hides.

**Where:** stage 6's standard-library tour and its kill criterion; stage 8's data model.

### Dreyfus model of skill acquisition — Dreyfus & Dreyfus (1980)

**Finding:** Skill develops from rule-following to situational judgment. Novices need rules; experts are hindered by them.

**Rule:** Tier A gives rules ("always read the whole error", "always run it"). Tier D asks for judgment ("should this be a class? Show two versions and their tests"). The kill criteria at every stage are the bridge: rules in the form of "when not to", which is how judgment first appears.

**Where:** Kill criteria; Tier D framing; the Programmer's Oath.

## What the evidence does *not* say

- Most learning-science findings above come from school and university settings on well-defined domains. Applied to a self-paced adult beginner, they are strong priors, not proof.
- There is no controlled study of this curriculum. It is a hypothesis. [11 — Curriculum maintenance](11-curriculum-maintenance.md) describes how learner data should be used to revise it.
- The 140-hour budget is an estimate from comparable beginner material scaled for the exercise volume. Track actuals in `LEDGER.md`.

## Design rules, consolidated

1. Worked example first; vary one thing at a time.
2. Break it before you are taught why.
3. Run it before you say it works; test it before you trust it.
4. Read the whole error, bottom up.
5. See inside the program: print, trace, debug, log, time.
6. Gate on criteria, not calendar; hidden inputs, not visible ones.
7. Fade the scaffolding as competence rises.
8. Spiral the strands; never silo them.
9. Make the learner explain, retrieve and teach.
10. Accept "do not write it" as a correct answer.
