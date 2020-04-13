import sys


def count_until_sam(list):
    """Returns how many words occur in list up to
    and including the first occurrence of 'sam'"""
    count = 0
    for item in list:
        count = count + 1
        if item == 'sam':
            return count
    return count


def test(did_pass):
    """Ṕrint the result of a test."""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    """Tests for count_until_sam function"""
    test(count_until_sam(['hello', 'how', 'are', 'you', 'sam']) == 5)
    test(count_until_sam([]) == 0)
    test(count_until_sam(['ola', 'sam']) == 2)
    test(count_until_sam(['sam', 'foi', 'a', 'praia']) == 1)


# Run the tests
test_suite()
