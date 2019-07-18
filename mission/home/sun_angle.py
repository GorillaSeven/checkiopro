# -*- coding: utf-8 -*-#
"""
#-------------------------------------------------------------------------------
# Name:         sun_angle
# Description:  计算太阳角度
# Author:       ZengJiangDong
# Date:         2019/7/18
#-------------------------------------------------------------------------------
"""


def sun_angle(time):
    #replace this for solution
    times = time.split(":")
    hour = int(times[0])
    minute = int(times[1])
    if hour == 18 and minute == 0:
        return 180
    elif hour < 6 or hour >= 18:
        return "I don\'t see the sun!"
    else:
        return ((hour - 6)*60 + minute)*0.25


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")