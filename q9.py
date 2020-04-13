import sys


def reverse(str):
    """Returns str string from right to left"""
    new_str = []
    for i in range(0, len(str)):
        new_str += str[len(str) - i - 1]
    return ''.join(new_str)


def is_palindrome(str):
    """Returns true if str is a palindrome. False otherwise. """
    if str == reverse(str):
        return True
    else:
        return False


def test(did_pass):
    """Ṕrint the result of a test."""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    """Tests for is_palindrome function"""
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))


#Run the tests
test_suite()