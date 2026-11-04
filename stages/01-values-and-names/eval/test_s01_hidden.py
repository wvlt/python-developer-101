"""Hidden tests for stage 1: run by `just eval 01`. Do not open before your gate (docs/06).

Case IDs are stable: s01-rMeK-x is rung M, exercise K, case x.
"""

import pytest

CASES = [
    pytest.param("r1e1_sum_and_product", "12\n12\n", "24\n144", id="s01-r1e1-a"),
    pytest.param("r1e1_sum_and_product", "-5\n3\n", "-2\n-15", id="s01-r1e1-b"),
    pytest.param(
        "r1e1_sum_and_product", "1000000\n1000000\n", "2000000\n1000000000000", id="s01-r1e1-c"
    ),
    pytest.param("r1e2_three_divisions", "-7\n2\n", "-3.5\n-4\n1", id="s01-r1e2-a"),
    pytest.param("r1e2_three_divisions", "1\n4\n", "0.25\n0\n1", id="s01-r1e2-b"),
    pytest.param("r1e2_three_divisions", "100\n7\n", "14.285714285714286\n14\n2", id="s01-r1e2-c"),
    pytest.param("r1e3_seconds_in", "24\n", "86400", id="s01-r1e3-a"),
    pytest.param("r1e3_seconds_in", "168\n", "604800", id="s01-r1e3-b"),
    pytest.param("r1e4_power_and_root", "9\n", "729\n3.0", id="s01-r1e4-a"),
    pytest.param("r1e4_power_and_root", "100\n", "1000000\n10.0", id="s01-r1e4-b"),
    pytest.param("r2e1_plus_one", "-1\n", "0", id="s01-r2e1-a"),
    pytest.param("r2e1_plus_one", "999\n", "1000", id="s01-r2e1-b"),
    pytest.param("r2e2_decimal_sum", "0.5\n0.25\n", "0.75", id="s01-r2e2-a"),
    pytest.param("r2e2_decimal_sum", "-1.5\n1.5\n", "0.0", id="s01-r2e2-b"),
    pytest.param("r2e3_twice_as_text", "100\n", "100100\n200", id="s01-r2e3-a"),
    pytest.param("r2e3_twice_as_text", "0\n", "00\n0", id="s01-r2e3-b"),
    pytest.param("r2e4_whole_part", "0.999\n", "0", id="s01-r2e4-a"),
    pytest.param("r2e4_whole_part", "12.0\n", "12", id="s01-r2e4-b"),
    pytest.param("r3e1_swap", "hello world\n!\n", "!\nhello world", id="s01-r3e1-a"),
    pytest.param("r3e1_swap", "same\nsame\n", "same\nsame", id="s01-r3e1-b"),
    pytest.param("r3e2_running_total", "-5\n5\n0\n", "-5\n0\n0", id="s01-r3e2-a"),
    pytest.param("r3e2_running_total", "100\n200\n300\n", "100\n300\n600", id="s01-r3e2-b"),
    pytest.param("r3e3_rectangle", "1\n1\n", "1\n4", id="s01-r3e3-a"),
    pytest.param("r3e3_rectangle", "12\n30\n", "360\n84", id="s01-r3e3-b"),
    pytest.param("r3e4_to_fahrenheit", "-40\n", "-40.0", id="s01-r3e4-a"),
    pytest.param("r3e4_to_fahrenheit", "37.5\n", "99.5", id="s01-r3e4-b"),
    pytest.param("r4e1_how_long", "\n", "0", id="s01-r4e1-a"),
    pytest.param("r4e1_how_long", "  two  spaces  \n", "15", id="s01-r4e1-b"),
    pytest.param("r4e2_first_and_last", "Ab\n", "A b", id="s01-r4e2-a"),
    pytest.param("r4e2_first_and_last", "level\n", "l l", id="s01-r4e2-b"),
    pytest.param("r4e3_inside", "abc\n", "b", id="s01-r4e3-a"),
    pytest.param("r4e3_inside", "[bracketed]\n", "bracketed", id="s01-r4e3-b"),
    pytest.param("r4e4_backwards", "racecar\n", "racecar", id="s01-r4e4-a"),
    pytest.param("r4e4_backwards", "12345\n", "54321", id="s01-r4e4-b"),
    pytest.param("r5e1_shout", "MiXeD 123\n", "MIXED 123\nmixed 123", id="s01-r5e1-a"),
    pytest.param("r5e1_shout", "ßtraße\n", "SSTRASSE\nßtraße", id="s01-r5e1-b"),
    pytest.param("r5e2_tidy_name", "\tMARGARET hamilton\n", "Margaret Hamilton", id="s01-r5e2-a"),
    pytest.param("r5e2_tidy_name", "x\n", "X", id="s01-r5e2-b"),
    pytest.param("r5e3_count_letter", "Mississippi\ns\n", "4", id="s01-r5e3-a"),
    pytest.param("r5e3_count_letter", "a a a\n \n", "2", id="s01-r5e3-b"),
    pytest.param("r5e4_cat_to_dog", "cat cat cat\n", "dog dog dog", id="s01-r5e4-a"),
    pytest.param("r5e4_cat_to_dog", "concatenate\n", "condogenate", id="s01-r5e4-b"),
    pytest.param("r5e5_is_python_file", "archive.py.bak\n", "False", id="s01-r5e5-a"),
    pytest.param("r5e5_is_python_file", "a.PY\n", "False", id="s01-r5e5-b"),
    pytest.param("r5e5_is_python_file", ".py\n", "True", id="s01-r5e5-c"),
    pytest.param(
        "r6e1_introduce", "Mary Anne\n101\n", "Mary Anne is 101 years old", id="s01-r6e1-a"
    ),
    pytest.param("r6e1_introduce", "X\n0\n", "X is 0 years old", id="s01-r6e1-b"),
    pytest.param("r6e2_price_tag", "0\n", "$0.00", id="s01-r6e2-a"),
    pytest.param("r6e2_price_tag", "2.345\n", "$2.35", id="s01-r6e2-b"),
    pytest.param("r6e2_price_tag", "0.005\n", "$0.01", id="s01-r6e2-c"),
    pytest.param("r6e3_table_row", "kiwi\n1\n0.333\n", "kiwi        1    0.33", id="s01-r6e3-a"),
    pytest.param(
        "r6e3_table_row", "watermelon\n100\n1234.5\n", "watermelon100 1234.50", id="s01-r6e3-b"
    ),
    pytest.param("r7e1_three_questions", "-1\n-2\n", "False\nFalse\nTrue", id="s01-r7e1-a"),
    pytest.param("r7e1_three_questions", "0\n0\n", "False\nTrue\nFalse", id="s01-r7e1-b"),
    pytest.param("r7e2_in_range", "1\n", "True", id="s01-r7e2-a"),
    pytest.param("r7e2_in_range", "10\n", "True", id="s01-r7e2-b"),
    pytest.param("r7e2_in_range", "0\n", "False", id="s01-r7e2-c"),
    pytest.param("r7e3_truth_of_text", "-1\n", "True\nTrue", id="s01-r7e3-a"),
    pytest.param("r7e3_truth_of_text", "00\n", "True\nFalse", id="s01-r7e3-b"),
    pytest.param("r7e4_same_ignoring_case", "SAME\nSAME\n", "True\nTrue", id="s01-r7e4-a"),
    pytest.param("r7e4_same_ignoring_case", "a \na\n", "False\nFalse", id="s01-r7e4-b"),
    pytest.param(
        "r9e1_receipt",
        "tea\n10\n0.1\ncoffee\n0\n4.5\nsugar\n1\n0.01\n",
        "Item      Qty   Price\ntea        10    1.00\ncoffee      0    0.00\nsugar       1    0.01\n---------------------\nTOTAL            1.01",
        id="s01-r9e1-a",
    ),
    pytest.param(
        "r9e1_receipt",
        "watermelon\n1\n6\nfig\n12\n0.75\nnuts\n2\n12.345\n",
        "Item      Qty   Price\nwatermelon  1    6.00\nfig        12    9.00\nnuts        2   24.69\n---------------------\nTOTAL           39.69",
        id="s01-r9e1-b",
    ),
]


@pytest.mark.parametrize(("name", "stdin", "expected"), CASES)
def test_hidden(run_exercise, name, stdin, expected):
    run_exercise(name, stdin, expected)
