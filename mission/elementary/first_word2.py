# -*- coding: utf-8 -*-#
"""
#-------------------------------------------------------------------------------
# Name:         first_word2
# Description:  
# Author:       ZengJiangDong
# Date:         2019/7/18
#-------------------------------------------------------------------------------
"""
import re

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    text = text.strip(" ,.")
    indexs = [text.find(" "), text.find(","), text.find(".")]
    filte_indexs = [x for x in indexs if x >= 0]
    if len(filte_indexs) == 0:
        return text
    return text[:min(filte_indexs)]


if __name__ == '__main__':
    print("Example:")
    # print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert first_word("Hello world") == "Hello"
    # assert first_word(" a word ") == "a"
    # assert first_word("don't touch it") == "don't"
    # assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")