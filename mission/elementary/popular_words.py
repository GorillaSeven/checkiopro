# -*- coding: utf-8 -*-#
"""
#-------------------------------------------------------------------------------
# Name:         popular_words
# Description:  
# Author:       ZengJiangDong
# Date:         2019/7/19
#-------------------------------------------------------------------------------
"""


def popular_words(text: str, words: list) -> dict:
    # your code here
    text1 = text[:]
    text2 = [x.lower() for x in text1.replace("\n"," ").strip().split(" ")]
    result = {}
    for str in words:
        result[str] = text2.count(str)
    return result


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")