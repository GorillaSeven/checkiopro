# -*- coding: utf-8 -*-#
"""
#-------------------------------------------------------------------------------
# Name:         even_the_last
# Description:  
# Author:       ZengJiangDong
# Date:         2019/7/18
#-------------------------------------------------------------------------------
"""


def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) > 0:
        result = 0
        for i in range(len(array)):
            if i % 2 == 0:
                result += array[i]
        result *= array[-1]
        return result
    return 0


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")