import sys
import math


def is_prime(num):
    """Returns true if num is prime. False otherwise"""
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        i = i + 1
    return True


def test(did_pass):
    """Ṕrint the result of a test."""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    """Tests for is_prime function"""
    test(is_prime(11))
    test(not is_prime(35))
    test(not is_prime(19980608))
    test(is_prime(3))
    test(is_prime(2))


# Run the tests
test_suite()
