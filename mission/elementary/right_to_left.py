# -*- coding: utf-8 -*-#
"""
#-------------------------------------------------------------------------------
# Name:         right_to_left
# Description:  
# Author:       ZengJiangDong
# Date:         2019/7/18
#-------------------------------------------------------------------------------
"""


def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    result = ''
    index = 0
    for x in phrases:
        if str(x).find("right") >= 0:
            result += str(x).replace("right", "left")
        else:
            result += str(x)
        if index < len(phrases)-1:
            result += ','
        index += 1
    return result


if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")