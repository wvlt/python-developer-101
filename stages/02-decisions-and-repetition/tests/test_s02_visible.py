"""Visible tests for stage 2: the ones each rung tells you to run with `just test 02`.

Each row is (exercise file, what is typed in, what must be printed). Read the rows before you start an
exercise; they are the examples. `just test 02 -k r4e` runs only rung 4's exercises.
"""

import pytest

CASES = [
    pytest.param("r1e1_pass_or_fail", "50\n", "pass", id="r1e1-a"),
    pytest.param("r1e1_pass_or_fail", "49\n", "fail", id="r1e1-b"),
    pytest.param("r1e2_even_or_odd", "4\n", "even", id="r1e2-a"),
    pytest.param("r1e2_even_or_odd", "7\n", "odd", id="r1e2-b"),
    pytest.param("r1e3_larger", "3\n9\n", "9", id="r1e3-a"),
    pytest.param("r1e3_larger", "5\n5\n", "same", id="r1e3-b"),
    pytest.param("r2e1_letter_grade", "85\n", "A", id="r2e1-a"),
    pytest.param("r2e1_letter_grade", "39\n", "F", id="r2e1-b"),
    pytest.param("r2e1_letter_grade", "70\n", "B", id="r2e1-c"),
    pytest.param("r2e2_sign", "3\n", "positive", id="r2e2-a"),
    pytest.param("r2e2_sign", "0\n", "zero", id="r2e2-b"),
    pytest.param("r2e3_fizz", "9\n", "Fizz", id="r2e3-a"),
    pytest.param("r2e3_fizz", "10\n", "10", id="r2e3-b"),
    pytest.param("r3e1_weekday", "1\n", "Monday", id="r3e1-a"),
    pytest.param("r3e1_weekday", "9\n", "unknown", id="r3e1-b"),
    pytest.param("r3e1_weekday", "7\n", "Sunday", id="r3e1-c"),
    pytest.param("r3e2_command", "n\n", "You walk north.", id="r3e2-a"),
    pytest.param("r3e2_command", "look\n", "You see a door.", id="r3e2-b"),
    pytest.param("r3e2_command", "dance\n", "I do not understand.", id="r3e2-c"),
    pytest.param("r4e1_until_stop", "a\nb\nstop\n", "2", id="r4e1-a"),
    pytest.param("r4e1_until_stop", "stop\n", "0", id="r4e1-b"),
    pytest.param(
        "r4e2_valid_number", "abc\n11\n5\n", "not a number\nout of range\nGot 5", id="r4e2-a"
    ),
    pytest.param("r4e2_valid_number", "10\n", "Got 10", id="r4e2-b"),
    pytest.param("r4e3_countdown", "3\n", "3\n2\n1\nGo", id="r4e3-a"),
    pytest.param("r4e3_countdown", "1\n", "1\nGo", id="r4e3-b"),
    pytest.param("r5e1_count_up", "3\n", "1\n2\n3", id="r5e1-a"),
    pytest.param("r5e1_count_up", "1\n", "1", id="r5e1-b"),
    pytest.param("r5e2_sum_to", "4\n", "10", id="r5e2-a"),
    pytest.param("r5e2_sum_to", "1\n", "1", id="r5e2-b"),
    pytest.param("r5e3_evens_between", "3\n8\n", "4\n6\n8", id="r5e3-a"),
    pytest.param("r5e3_evens_between", "2\n2\n", "2", id="r5e3-b"),
    pytest.param(
        "r5e4_times_table",
        "2\n",
        "2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n2 x 4 = 8\n2 x 5 = 10\n2 x 6 = 12\n2 x 7 = 14\n2 x 8 = 16\n2 x 9 = 18\n2 x 10 = 20",
        id="r5e4-a",
    ),
    pytest.param("r6e1_first_multiple_over", "7\n100\n", "105", id="r6e1-a"),
    pytest.param("r6e1_first_multiple_over", "5\n5\n", "10", id="r6e1-b"),
    pytest.param("r6e2_skip_threes", "7\n", "1\n2\n4\n5\n7", id="r6e2-a"),
    pytest.param("r6e2_skip_threes", "3\n", "1\n2", id="r6e2-b"),
    pytest.param("r6e3_is_prime", "7\n", "prime", id="r6e3-a"),
    pytest.param("r6e3_is_prime", "9\n", "not prime", id="r6e3-b"),
    pytest.param("r7e1_numbered_lines", "2\napple\npear\n", "1. apple\n2. pear", id="r7e1-a"),
    pytest.param("r7e1_numbered_lines", "1\nonly\n", "1. only", id="r7e1-b"),
    pytest.param("r7e2_names_and_scores", "2\nAda\nBob\n90\n75\n", "Ada: 90\nBob: 75", id="r7e2-a"),
    pytest.param("r7e2_names_and_scores", "1\nX\n0\n", "X: 0", id="r7e2-b"),
    pytest.param("r8e1_largest", "3\n4\n9\n2\n", "9", id="r8e1-a"),
    pytest.param("r8e1_largest", "1\n-5\n", "-5", id="r8e1-b"),
    pytest.param("r8e2_count_vowels", "Hello World\n", "3", id="r8e2-a"),
    pytest.param("r8e2_count_vowels", "xyz\n", "0", id="r8e2-b"),
    pytest.param("r8e3_star_box", "3\n2\n", "***\n***", id="r8e3-a"),
    pytest.param("r8e3_star_box", "1\n1\n", "*", id="r8e3-b"),
    pytest.param("r8e4_any_negative", "3\n1\n-2\n3\n", "yes", id="r8e4-a"),
    pytest.param("r8e4_any_negative", "2\n0\n5\n", "no", id="r8e4-b"),
    pytest.param("r9b1_total_bug", "3\n4\n9\n2\n", "15\n9", id="r9b1-a"),
    pytest.param("r9b1_total_bug", "2\n-5\n-3\n", "-8\n-3", id="r9b1-b"),
    pytest.param(
        "r11e1_guess_the_number",
        "42\n50\nabc\n25\n42\n",
        "lower\nnumbers only\nhigher\ncorrect in 3",
        id="r11e1-a",
    ),
    pytest.param("r11e1_guess_the_number", "1\n1\n", "correct in 1", id="r11e1-b"),
]


@pytest.mark.parametrize(("name", "stdin", "expected"), CASES)
def test_exercise(run_exercise, name, stdin, expected):
    run_exercise(name, stdin, expected)
