# -*- coding: utf-8 -*-#
"""
#-------------------------------------------------------------------------------
# Name:         long_repeat
# Description:  找到字符串中最长的相同字符重复出现的次数，并返回它的重复次数
# Author:       ZengJiangDong
# Date:         2019/7/18
#-------------------------------------------------------------------------------
"""


def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    if len(line) == 0 or line.isspace():
        return 0
    value = 0
    max = 0
    last = line[0]
    for char in line:
        if last == char:
            value += 1
            if max < value:
                max = value
        else:
            last = char
            value = 1
    return max


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')