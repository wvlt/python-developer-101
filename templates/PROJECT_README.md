# <program name>

> Template for the README of your mini-project (stage 6 onward) and the capstone. Written for a stranger who has the repository and nothing else. Test: hand it to a peer in the break-my-program session; if they cannot run the program from this file alone, it is not done. Delete this quote block.

One sentence: what the program does and for whom.

## Install

Exact commands from a fresh clone. Say what you should see after each.

```
uv sync
just data
uv run <name> --help
```

Expect: the help text listing the sub-commands below.

## Use

One example per sub-command, with the output it produces on the fixture.

```
uv run <name> report --as-of 2026-03-01
```

```
<the first five lines of real output>
```

## Inputs it accepts

| Input | Where it comes from | What happens if it is missing or malformed |
|---|---|---|
| `books.csv` | `data/library/` or `--data-dir` | missing: error naming the path, exit 1; bad row: skipped and logged with its line number |
| | | |

## Configuration

Environment variables read, with defaults. Copy of the relevant lines from `.env.example`.

## How it is tested

```
just test NN
just eval NN
```

Current counts: `<n>` of `<m>` hidden; coverage `<p>` %. Last run: `eval/runs/<dir>`.

## How it fails

The three inputs most likely to break it and what it does today (from the Artefact Card). Where to look when it does: the log file, the `--verbose` flag.

## Design

Three to five sentences on the shape: modules, the main classes, where data lives, what is persisted and in which format. Link the ADRs.

## Not done / known limits

Honest list. What it does not handle and whether that is a decision or a gap.

## Licence

