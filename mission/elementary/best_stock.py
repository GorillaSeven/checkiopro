# -*- coding: utf-8 -*-#
"""
#-------------------------------------------------------------------------------
# Name:         best_stock
# Description:  
# Author:       ZengJiangDong
# Date:         2019/7/18
#-------------------------------------------------------------------------------
"""


def best_stock(data):
    # your code here
    data_sorted = dict(sorted(data.items(),key=lambda x: x[1],reverse=True))
    keys = list(data_sorted.keys())
    return keys[0]


if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")
