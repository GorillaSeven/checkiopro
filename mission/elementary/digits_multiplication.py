# -*- coding: utf-8 -*-#
"""
#-------------------------------------------------------------------------------
# Name:         digits_multiplication
# Description:  
# Author:       ZengJiangDong
# Date:         2019/7/18
#-------------------------------------------------------------------------------
"""


def checkio(number: int) -> int:
    numbers = [int(x) for x in str(number) if int(x) != 0]
    result = 1
    for n in numbers:
        result *= n
    return result


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")