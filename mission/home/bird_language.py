# -*- coding: utf-8 -*-#
"""
#-------------------------------------------------------------------------------
# Name:         bird_language
# Description:  
# Author:       ZengJiangDong
# Date:         2019/7/18
#-------------------------------------------------------------------------------
"""
import re


VOWELS = "[aeiouy]"

def translate(phrase):
    result = ''
    index = 0
    for i in range(len(phrase)):
        if index >= len(phrase):
            break
        result += phrase[index]
        if phrase[index].isalpha():
            if re.match(VOWELS, phrase[index]):
                #元音
                index += 3
            else:
                index += 2
        else:
            index += 1
    return result


if __name__ == '__main__':
    print("Example:")
    # print(translate("hieeelalaooo"))
    #
    # #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")