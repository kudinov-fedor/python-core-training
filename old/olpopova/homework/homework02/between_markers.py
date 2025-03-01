"""
**********************************************************************
You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.

The initial and final markers are always different.
The initial and final markers are always 1 char size.
The initial and final markers always exist in a string and go one after another.
*********************************************************************
"""


def between_markers(text: str, start: str, end: str) -> str:
    return text[text.index(start)+1:text.index(end)]
