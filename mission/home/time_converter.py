# -*- coding: utf-8 -*-#
"""
#-------------------------------------------------------------------------------
# Name:         time_converter
# Description:  
# Author:       ZengJiangDong
# Date:         2019/7/17
#-------------------------------------------------------------------------------
"""

def time_converter(time):
    times = time.split(":")
    profix = "a.m." if 0 <= int(times[0]) < 12 else "p.m."
    hour = int(times[0]) if int(times[0]) <= 12 else int(times[0]) - 12
    if int(times[0]) == 0:
        hour = 12
    return '%s:%s %s' % (hour, times[1], profix)


if __name__ == '__main__':
    print("Example:")
    print(time_converter('0:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")