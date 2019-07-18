# -*- coding: utf-8 -*-#
"""
#-------------------------------------------------------------------------------
# Name:         sort_array_by_element_frequency
# Description:  
# Author:       ZengJiangDong
# Date:         2019/7/17
#-------------------------------------------------------------------------------
"""


def frequency_sort(items):
    # your code here
    counter = {x: items.count(x) for x in items}
    sorted_counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
    result = []
    for key,value in sorted_counter.items():
        for i in range(value):
            result.append(key)
    return result


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6,2, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")