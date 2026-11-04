"""Hidden tests for stage 2: run by `just eval 02`. Do not open before your gate (docs/06).

Case IDs are stable: s02-rMeK-x is rung M, exercise K, case x.
"""

import pytest

CASES = [
    pytest.param("r1e1_pass_or_fail", "100\n", "pass", id="s02-r1e1-a"),
    pytest.param("r1e1_pass_or_fail", "0\n", "fail", id="s02-r1e1-b"),
    pytest.param("r1e1_pass_or_fail", "51\n", "pass", id="s02-r1e1-c"),
    pytest.param("r1e2_even_or_odd", "0\n", "even", id="s02-r1e2-a"),
    pytest.param("r1e2_even_or_odd", "-3\n", "odd", id="s02-r1e2-b"),
    pytest.param("r1e3_larger", "-1\n-2\n", "-1", id="s02-r1e3-a"),
    pytest.param("r1e3_larger", "10\n2\n", "10", id="s02-r1e3-b"),
    pytest.param("r2e1_letter_grade", "84\n", "B", id="s02-r2e1-a"),
    pytest.param("r2e1_letter_grade", "55\n", "C", id="s02-r2e1-b"),
    pytest.param("r2e1_letter_grade", "40\n", "D", id="s02-r2e1-c"),
    pytest.param("r2e1_letter_grade", "100\n", "A", id="s02-r2e1-d"),
    pytest.param("r2e2_sign", "-7\n", "negative", id="s02-r2e2-a"),
    pytest.param("r2e2_sign", "1\n", "positive", id="s02-r2e2-b"),
    pytest.param("r2e3_fizz", "0\n", "Fizz", id="s02-r2e3-a"),
    pytest.param("r2e3_fizz", "-6\n", "Fizz", id="s02-r2e3-b"),
    pytest.param("r2e3_fizz", "7\n", "7", id="s02-r2e3-c"),
    pytest.param("r3e1_weekday", "3\n", "Wednesday", id="s02-r3e1-a"),
    pytest.param("r3e1_weekday", "0\n", "unknown", id="s02-r3e1-b"),
    pytest.param("r3e1_weekday", "6\n", "Saturday", id="s02-r3e1-c"),
    pytest.param("r3e2_command", "north\n", "You walk north.", id="s02-r3e2-a"),
    pytest.param("r3e2_command", "quit\n", "Goodbye.", id="s02-r3e2-b"),
    pytest.param("r3e2_command", "LOOK\n", "I do not understand.", id="s02-r3e2-c"),
    pytest.param("r4e1_until_stop", "x\nx\nx\nx\nstop\n", "4", id="s02-r4e1-a"),
    pytest.param("r4e1_until_stop", "Stop\nstop\n", "1", id="s02-r4e1-b"),
    pytest.param("r4e2_valid_number", "0\n1\n", "out of range\nGot 1", id="s02-r4e2-a"),
    pytest.param(
        "r4e2_valid_number", "\n-3\n3\n", "not a number\nnot a number\nGot 3", id="s02-r4e2-b"
    ),
    pytest.param("r4e2_valid_number", "7.5\n07\n", "not a number\nGot 7", id="s02-r4e2-c"),
    pytest.param("r4e3_countdown", "5\n", "5\n4\n3\n2\n1\nGo", id="s02-r4e3-a"),
    pytest.param("r4e3_countdown", "0\n", "Go", id="s02-r4e3-b"),
    pytest.param("r5e1_count_up", "5\n", "1\n2\n3\n4\n5", id="s02-r5e1-a"),
    pytest.param("r5e1_count_up", "0\n", "", id="s02-r5e1-b"),
    pytest.param("r5e2_sum_to", "100\n", "5050", id="s02-r5e2-a"),
    pytest.param("r5e2_sum_to", "0\n", "0", id="s02-r5e2-b"),
    pytest.param("r5e3_evens_between", "-4\n1\n", "-4\n-2\n0", id="s02-r5e3-a"),
    pytest.param("r5e3_evens_between", "7\n7\n", "", id="s02-r5e3-b"),
    pytest.param(
        "r5e4_times_table",
        "7\n",
        "7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21\n7 x 4 = 28\n7 x 5 = 35\n7 x 6 = 42\n7 x 7 = 49\n7 x 8 = 56\n7 x 9 = 63\n7 x 10 = 70",
        id="s02-r5e4-a",
    ),
    pytest.param(
        "r5e4_times_table",
        "0\n",
        "0 x 1 = 0\n0 x 2 = 0\n0 x 3 = 0\n0 x 4 = 0\n0 x 5 = 0\n0 x 6 = 0\n0 x 7 = 0\n0 x 8 = 0\n0 x 9 = 0\n0 x 10 = 0",
        id="s02-r5e4-b",
    ),
    pytest.param("r6e1_first_multiple_over", "1\n0\n", "1", id="s02-r6e1-a"),
    pytest.param("r6e1_first_multiple_over", "12\n143\n", "144", id="s02-r6e1-b"),
    pytest.param("r6e2_skip_threes", "10\n", "1\n2\n4\n5\n7\n8\n10", id="s02-r6e2-a"),
    pytest.param("r6e2_skip_threes", "2\n", "1\n2", id="s02-r6e2-b"),
    pytest.param("r6e3_is_prime", "2\n", "prime", id="s02-r6e3-a"),
    pytest.param("r6e3_is_prime", "97\n", "prime", id="s02-r6e3-b"),
    pytest.param("r6e3_is_prime", "91\n", "not prime", id="s02-r6e3-c"),
    pytest.param("r7e1_numbered_lines", "3\na\nb\nc\n", "1. a\n2. b\n3. c", id="s02-r7e1-a"),
    pytest.param("r7e1_numbered_lines", "0\n", "", id="s02-r7e1-b"),
    pytest.param(
        "r7e2_names_and_scores", "3\na\nb\nc\n1\n2\n3\n", "a: 1\nb: 2\nc: 3", id="s02-r7e2-a"
    ),
    pytest.param("r7e2_names_and_scores", "0\n", "", id="s02-r7e2-b"),
    pytest.param("r8e1_largest", "4\n-3\n-1\n-2\n-9\n", "-1", id="s02-r8e1-a"),
    pytest.param("r8e1_largest", "3\n5\n5\n5\n", "5", id="s02-r8e1-b"),
    pytest.param("r8e2_count_vowels", "AEIOU aeiou\n", "10", id="s02-r8e2-a"),
    pytest.param("r8e2_count_vowels", "\n", "0", id="s02-r8e2-b"),
    pytest.param("r8e3_star_box", "5\n3\n", "*****\n*****\n*****", id="s02-r8e3-a"),
    pytest.param("r8e3_star_box", "2\n4\n", "**\n**\n**\n**", id="s02-r8e3-b"),
    pytest.param("r8e4_any_negative", "1\n-1\n", "yes", id="s02-r8e4-a"),
    pytest.param("r8e4_any_negative", "0\n", "no", id="s02-r8e4-b"),
    pytest.param("r8e4_any_negative", "4\n1\n2\n3\n-4\n", "yes", id="s02-r8e4-c"),
    pytest.param("r9b1_total_bug", "4\n-1\n-2\n-3\n-4\n", "-10\n-1", id="s02-r9b1-a"),
    pytest.param("r9b1_total_bug", "2\n0\n0\n", "0\n0", id="s02-r9b1-b"),
    pytest.param(
        "r11e1_guess_the_number",
        "100\n0\n101\n100\n",
        "between 1 and 100\nbetween 1 and 100\ncorrect in 1",
        id="s02-r11e1-a",
    ),
    pytest.param(
        "r11e1_guess_the_number", "7\n-7\n7\n", "numbers only\ncorrect in 1", id="s02-r11e1-b"
    ),
    pytest.param(
        "r11e1_guess_the_number",
        "50\n49\n51\n50\n",
        "higher\nlower\ncorrect in 3",
        id="s02-r11e1-c",
    ),
]


@pytest.mark.parametrize(("name", "stdin", "expected"), CASES)
def test_hidden(run_exercise, name, stdin, expected):
    run_exercise(name, stdin, expected)
