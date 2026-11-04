# Error analysis — <program or package> — <date>

> For the stage 9 planted-bug hunt and any time a program fails more than a handful of tests. Three-line summary first: what was measured, what was found, what was changed.

**Measured:** `<program>` against `<test set>`, n=`<n>` tests, `<f>` failing, run `eval/runs/<dir>`.
**Found:** `<f>` failures classified into `<k>` bestiary categories; the largest was `<category>` with `<count>`.
**Changed:** `<fixes>`; now `<n − remaining>` passing, run `eval/runs/<dir>`.

## 1. Setup

- Program and commit:
- Test set (visible / hidden / my own) and count:
- Tools used to find each bug (traceback / debugger / logging / `timeit` / reading):

## 2. Failure collection

Every failing test, one row, written *before* fixing anything. The code column is one sentence saying what is wrong, not how to fix it.

| Test or case ID | Symptom (first line of the failure) | Code (one sentence: what went wrong) |
|---|---|---|
| s09-r11e1-a | `assert overdue(...) == 3` got 4 | Loop counts the boundary day as overdue; half-open range misread. |
| | | |

## 3. Classification

Group the codes by bestiary ID. A failure that fits no entry gets a proposed new ID and a snippet.

| Bestiary ID | Name | Count | Loud / quiet | Example test |
|---|---|---|---|---|
| F01 | Off-by-one | | quiet | |
| | | | | |

## 4. Time per bug

| Bug | Minutes to locate | Minutes to fix | Tool that found it |
|---|---|---|---|
| | | | |

The slowest bug: what made it slow? Was it quiet? Which Inspect tool would have found it faster?

## 5. The fixes

For each bug: the test that now fails before the fix and passes after (its ID), and the one-line diff or a link to the commit.

| Bug | Test added or used | Commit |
|---|---|---|
| | | |

## 6. Re-measurement

| | Before | After |
|---|---|---|
| Tests passing | | |
| Quiet failures remaining | | |
| Coverage (if measured) | | |

## 7. What the tests missed

Bugs found by reading or by the debugger that no test caught. For each: the test you added, and why it did not exist before.

## 8. Next

The bestiary category you will meet again. What habit (Oath item, `ruff` rule, test pattern) prevents it.
