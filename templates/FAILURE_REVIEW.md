# Failure review — <program> — <date>

> Where could this program be quietly wrong? Written *before* building (stage 10) or before the gate (stage 5 onward, recommended). The quiet failures are the ones that raise nothing; this document is the course's risk model, applied to one program. List is in [docs/07](../docs/07-failure-bestiary.md#q--the-quiet-failures-the-risk-model).

- **Program:** · **Stage:** · **Author:**
- **Commit reviewed:**

## 1. What the program touches

Every function that takes something from outside the program (a file, `input()`, an argument, an environment variable, the network) or writes something outside it, with its reach.

| Function | Reads | Writes | Worst thing a bad input could do |
|---|---|---|---|
| `load_loans(path)` | `loans.txt` | nothing | a bad line silently dropped; totals wrong |
| | | | |

## 2. The quiet failures, one by one

For each row: could it happen here? If yes, what **prevents** it: a test (name it), a structure (say which: "returns a new list", "`default_factory`", "`encoding='utf-8'` on every open"), or nothing yet.

| ID | Quiet failure | Could it happen here? | Prevented by | Type (structure / test / none) |
|---|---|---|---|---|
| C01 | Aliasing: a caller's list mutated | | | |
| N02 | Mutable default argument | | | |
| T05 | `is` where `==` was meant | | | |
| T04 | Float arithmetic on money or comparison with `==` | | | |
| T03 | `/` where `//` was meant, or the reverse; negative division | | | |
| F01 | Off-by-one in a range, slice or date boundary | | | |
| F04 | A built-in shadowed | | | |
| E01 | An exception caught and discarded | | | |
| N04 | A closure capturing a loop variable | | | |
| F05 | A collection changed while being iterated | | | |
| E02 | A file read without an explicit encoding, or errors silenced | | | |
| E06 | `pickle.load` of a file the program did not write | | | |
| E07 | `eval` or `exec` on anything from outside | | | |
| T02 | Text compared as a number, or a number as text | | | |
| T06 | Zero or empty treated as "missing" | | | |
| F03 | `x == a or b` | | | |
| C02 | Result of `.sort()` used | | | |
| C04 | Nested structure shallow-copied | | | |
| N01 | A function that prints instead of returning, or returns `None` on one path | | | |
| O02 | A mutable class attribute shared by instances | | | |

Structure beats tests: a function that cannot alias because it returns a new list needs no aliasing test. Mark which rows are prevented by structure and which only by a test.

## 3. Inputs I expect to be tried against it

The ten inputs a breaker would reach for first (see the [protocol](../docs/10-instructor-guide.md#break-my-program-protocol)), and what the program does on each today.

| Input | Expected behaviour | Actual (if tried) | Test exists? |
|---|---|---|---|
| empty file | | | |
| the four broken fixtures | | | |
| a date in the future | | | |
| the same ID twice | | | |
| Unicode in a name | | | |
| a negative or zero quantity | | | |
| `--count abc` | | | |
| run from another directory | | | |
| run twice (idempotence) | | | |
| Ctrl-C during a write | | | |

## 4. Residual risk

What is not prevented and not tested, and why that is acceptable for this program (or is not, and is on the list).

## 5. After the break-my-program session

Filled in afterwards. Findings that were: (a) anticipated above and prevented; (b) anticipated and not prevented; (c) not anticipated. Count each. List (c) is the lesson; each entry there becomes a row in section 2 or a bestiary proposal.
