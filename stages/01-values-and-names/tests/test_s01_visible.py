"""Visible tests for stage 1: the ones each rung tells you to run with `just test 01`.

Each row is (exercise file, what is typed in, what must be printed). Read the rows before you start an
exercise; they are the examples. `just test 01 -k r4e` runs only rung 4's exercises.
"""
import pytest

CASES = [
    pytest.param("r1e1_sum_and_product", "3\n4\n", "7\n12", id="r1e1-a"),
    pytest.param("r1e1_sum_and_product", "10\n0\n", "10\n0", id="r1e1-b"),
    pytest.param("r1e2_three_divisions", "7\n2\n", "3.5\n3\n1", id="r1e2-a"),
    pytest.param("r1e2_three_divisions", "9\n3\n", "3.0\n3\n0", id="r1e2-b"),
    pytest.param("r1e3_seconds_in", "2\n", "7200", id="r1e3-a"),
    pytest.param("r1e3_seconds_in", "0\n", "0", id="r1e3-b"),
    pytest.param("r1e4_power_and_root", "4\n", "64\n2.0", id="r1e4-a"),
    pytest.param("r1e4_power_and_root", "1\n", "1\n1.0", id="r1e4-b"),
    pytest.param("r2e1_plus_one", "41\n", "42", id="r2e1-a"),
    pytest.param("r2e1_plus_one", "0\n", "1", id="r2e1-b"),
    pytest.param("r2e2_decimal_sum", "1.5\n2.25\n", "3.75", id="r2e2-a"),
    pytest.param("r2e2_decimal_sum", "10\n0.5\n", "10.5", id="r2e2-b"),
    pytest.param("r2e3_twice_as_text", "12\n", "1212\n24", id="r2e3-a"),
    pytest.param("r2e3_twice_as_text", "7\n", "77\n14", id="r2e3-b"),
    pytest.param("r2e4_whole_part", "3.7\n", "3", id="r2e4-a"),
    pytest.param("r2e4_whole_part", "-3.7\n", "-3", id="r2e4-b"),
    pytest.param("r3e1_swap", "cat\ndog\n", "dog\ncat", id="r3e1-a"),
    pytest.param("r3e1_swap", "1\n2\n", "2\n1", id="r3e1-b"),
    pytest.param("r3e2_running_total", "5\n10\n20\n", "5\n15\n35", id="r3e2-a"),
    pytest.param("r3e2_running_total", "1\n1\n1\n", "1\n2\n3", id="r3e2-b"),
    pytest.param("r3e3_rectangle", "3\n4\n", "12\n14", id="r3e3-a"),
    pytest.param("r3e3_rectangle", "5\n5\n", "25\n20", id="r3e3-b"),
    pytest.param("r3e4_to_fahrenheit", "100\n", "212.0", id="r3e4-a"),
    pytest.param("r3e4_to_fahrenheit", "0\n", "32.0", id="r3e4-b"),
    pytest.param("r4e1_how_long", "hello world\n", "11", id="r4e1-a"),
    pytest.param("r4e1_how_long", "a\n", "1", id="r4e1-b"),
    pytest.param("r4e2_first_and_last", "python\n", "p n", id="r4e2-a"),
    pytest.param("r4e2_first_and_last", "a\n", "a a", id="r4e2-b"),
    pytest.param("r4e3_inside", "python\n", "ytho", id="r4e3-a"),
    pytest.param("r4e3_inside", "ab\n", "", id="r4e3-b"),
    pytest.param("r4e4_backwards", "stressed\n", "desserts", id="r4e4-a"),
    pytest.param("r4e4_backwards", "ab c\n", "c ba", id="r4e4-b"),
    pytest.param("r5e1_shout", "Hello\n", "HELLO\nhello", id="r5e1-a"),
    pytest.param("r5e1_shout", "abc\n", "ABC\nabc", id="r5e1-b"),
    pytest.param("r5e2_tidy_name", "  ada LOVELACE \n", "Ada Lovelace", id="r5e2-a"),
    pytest.param("r5e2_tidy_name", "grace hopper\n", "Grace Hopper", id="r5e2-b"),
    pytest.param("r5e3_count_letter", "banana\na\n", "3", id="r5e3-a"),
    pytest.param("r5e3_count_letter", "hello\nz\n", "0", id="r5e3-b"),
    pytest.param("r5e4_cat_to_dog", "the cat sat\n", "the dog sat", id="r5e4-a"),
    pytest.param("r5e4_cat_to_dog", "no felines here\n", "no felines here", id="r5e4-b"),
    pytest.param("r5e5_is_python_file", "hello.py\n", "True", id="r5e5-a"),
    pytest.param("r5e5_is_python_file", "notes.txt\n", "False", id="r5e5-b"),
    pytest.param("r6e1_introduce", "Ada\n36\n", "Ada is 36 years old", id="r6e1-a"),
    pytest.param("r6e1_introduce", "Bo\n7\n", "Bo is 7 years old", id="r6e1-b"),
    pytest.param("r6e2_price_tag", "4.5\n", "$4.50", id="r6e2-a"),
    pytest.param("r6e2_price_tag", "1234.567\n", "$1234.57", id="r6e2-b"),
    pytest.param("r6e3_table_row", "apple\n3\n0.5\n", "apple       3    0.50", id="r6e3-a"),
    pytest.param("r6e3_table_row", "pear\n12\n10\n", "pear       12   10.00", id="r6e3-b"),
    pytest.param("r7e1_three_questions", "2\n3\n", "True\nFalse\nTrue", id="r7e1-a"),
    pytest.param("r7e1_three_questions", "5\n5\n", "False\nTrue\nFalse", id="r7e1-b"),
    pytest.param("r7e2_in_range", "7\n", "True", id="r7e2-a"),
    pytest.param("r7e2_in_range", "11\n", "False", id="r7e2-b"),
    pytest.param("r7e3_truth_of_text", "5\n", "True\nTrue", id="r7e3-a"),
    pytest.param("r7e3_truth_of_text", "0\n", "True\nFalse", id="r7e3-b"),
    pytest.param("r7e4_same_ignoring_case", "Hello\nhello\n", "False\nTrue", id="r7e4-a"),
    pytest.param("r7e4_same_ignoring_case", "x\ny\n", "False\nFalse", id="r7e4-b"),
    pytest.param("r9e1_receipt", "apple\n3\n0.5\nbread\n1\n3.2\nmilk\n2\n1.25\n", "Item      Qty   Price\napple       3    1.50\nbread       1    3.20\nmilk        2    2.50\n---------------------\nTOTAL            7.20", id="r9e1-a"),
]


@pytest.mark.parametrize(("name", "stdin", "expected"), CASES)
def test_exercise(run_exercise, name, stdin, expected):
    run_exercise(name, stdin, expected)
