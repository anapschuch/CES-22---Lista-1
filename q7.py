import sys


def sum_of_squares(xs):
    """Returns the sum of the squares of the numbers
    in the list xs"""
    value = 0
    for item in xs:
        value = value + item**2
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
    """Tests for sum_of_squares function"""
    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([ ]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)


#Run the tests
test_suite()