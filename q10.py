import sys


def sum_complex_numbers(a, b):
    """a and b represent complex numbers, each one
    in the form (x,y). This function returns their sum."""
    return (a[0]+b[0], a[1]+b[1])


def test(did_pass):
    """Ṕrint the result of a test."""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    """Tests for sum_complex_numbers function"""
    test(sum_complex_numbers((1,2), (3,4)) == (4,6))
    test(sum_complex_numbers((1, 2), (1, 1)) == (2, 3))
    test(sum_complex_numbers((1, 2), (-1, 0)) == (0, 2))
    test(sum_complex_numbers((0,0), (0,0)) == (0,0))


test_suite()