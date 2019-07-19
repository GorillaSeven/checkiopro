# -*- coding: utf-8 -*-#
"""
#-------------------------------------------------------------------------------
# Name:         between_markers2
# Description:  
# Author:       ZengJiangDong
# Date:         2019/7/19
#-------------------------------------------------------------------------------
"""


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    begin_index = text.find(begin)
    end_index = text.find(end)
    if begin_index < 0 and end_index < 0:
        return text
    elif begin_index >= 0 and end_index < 0:
        return text[begin_index+len(begin):]
    elif begin_index < 0 and end_index >= 0:
        return text[:end_index]
    else:
        return text[begin_index+len(begin):end_index]
    if end_index > begin_index:
        return ''
    return ''


if __name__ == '__main__':
    print('Example:')
    # print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    # assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    # assert between_markers("<head><title>My new site</title></head>",
    #                        "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
