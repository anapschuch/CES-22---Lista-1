import sys


def sum_of_odds(list):
    """Returns the sum of all elements in list up to but
     not including the first even number"""
    value = 0
    for item in list:
        if item % 2 == 0:
            return value
        value = value + item
    return value


def test(did_pass):
    """Ṕrint the result of a test."""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    """Tests for sum_of_odds function"""
    test(sum_of_odds([2, 3, 4]) == 0)
    test(sum_of_odds([]) == 0)
    test(sum_of_odds([1, 3, 5, 7, 10, 11]) == 16)
    test(sum_of_odds([1, 3, 5, 7, 11]) == 27)
    test(sum_of_odds([1, 2, 5, 7, 10, 11]) == 1)


# Run the tests
test_suite()
