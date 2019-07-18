# -*- coding: utf-8 -*-#
"""
#-------------------------------------------------------------------------------
# Name:         flatten_a_list
# Description:  
# Author:       ZengJiangDong
# Date:         2019/7/18
#-------------------------------------------------------------------------------
"""


def flat_list(array):
    result = []
    flat_a_list(array, result)
    return result


def flat_a_list(array, result: list):
    if isinstance(array, list):
        for var in array:
            flat_a_list(var, result)
    else:
        result.append(array)


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')