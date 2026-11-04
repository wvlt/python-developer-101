# Artefact Card — Stage NN: <name>

> One page. Every field filled. "TBD" is a gate failure. Every number names the run directory it came from.

## Identity

- **Stage:** NN — <name>
- **Author:**
- **Curriculum version:** (git tag of upstream you started on)
- **Date passed gate:**
- **Commit:** (SHA on `main` after merge)

## What it does

Two sentences, for a stranger who does not program. What goes in, what comes out, what it is for.

## How to run it

The exact command, from a fresh clone, and one line of expected output.

```
just data
uv run <command>
```

## How it was tested

| Set | Passed | Of | Run directory |
|---|---|---|---|
| Visible (`just test NN`) | | | — |
| Hidden (`just eval NN`) | | | `eval/runs/<dir>` |
| My own tests (stage 6 onward) | | | |
| Of mine that catch the planted bug (stage 6) | | | |
| Coverage (stage 9 onward) | | % | |

One test that found a real bug in my code, and what the bug was:

## How it fails

The three inputs most likely to break it, tried, with what happened. Name the bestiary ID.

| Input | What happened | Loud / quiet | Bestiary | Status (fixed / handled / open) |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

## What I looked at inside it

Which Inspect tool this stage (f-string print / `just trace` / debugger / logging / `timeit`), on which line, and what it showed that I did not expect.

## What was decided

From stage 7: links to ADRs in `decisions/`, one line each. Before stage 7: the one structural choice you made (loop vs chain of `if`; list vs dict) and why in ten words.

- ADR-001 — <title> — <decision in ten words>

## Kill criteria

When would you *not* write this program? Answer for this problem: would a spreadsheet, a shell one-liner or a standard-library call have done it? If you ran it once, would you have written it?

## AI assistance

Through stage 6: confirm no code was written or suggested by an assistant; list anything an assistant explained (an error message, a concept). From stage 7: what you asked it to review, what it said, and what you changed or declined to change.

## Pins

Python and tool versions as in `PINS.md` at the commit above. Any deviation (a different Python patch; a tool version) and why.

## What I would do with one more day

Three bullets, in priority order, each tied to a failing input or a test.
