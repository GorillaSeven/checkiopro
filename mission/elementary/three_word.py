# -*- coding: utf-8 -*-#
"""
#-------------------------------------------------------------------------------
# Name:         three_word
# Description:  连续的三个单词
# Author:       ZengJiangDong
# Date:         2019/7/19
#-------------------------------------------------------------------------------
"""


def checkio(words: str) -> bool:
    var = [x.isalpha() for x in words.split(" ")]
    index = 0
    max = 0
    for v in var:
        if v:
            index += 1
            if index > max:
                max = index
        else:
            index = 0
    return max >= 3


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")