# -*- coding: utf-8 -*-#
"""
#-------------------------------------------------------------------------------
# Name:         most_wanted_letter.py
# Description:  The Most Wanted Letter
﻿

给你一段文本，其中包含不同的英文字母和标点符号。
你要找到其中那个出现最多的 字母，返回的字母必须是 小写形式。
找这个“头号通缉字母”时，大小写不重要，所以对于你的搜索而言 "A" == "a"。 注意不要管标点符号、数字和空格，我们只要 字母！

如果你找到 两个或两个以上出现频率相同的字母， 那么返回字母表中靠前的那个。 例如“one”包含“o”、“n”、“e”每个字母一次，因此我们选择“e”


# Author:       ZengJiangDong
# Date:         2019/7/17
#-------------------------------------------------------------------------------
"""
import string

def checkio(text: str) -> str:
    # textm = [c.lower() for c in text if c.isalpha()]
    # textm2 = {x: textm.count(x) for x in sorted(textm)}
    # for element in textm2:
    #     if textm2.get(element) == max(textm2.values()):
    #         return element
    text = text.lower()
    return max(string.ascii_lowercase,key=text.count)


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")