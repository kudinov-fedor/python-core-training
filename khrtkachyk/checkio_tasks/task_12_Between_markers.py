"""
You are given a string and two markers (the initial one and final). You have to find a substring enclosed
    between these two markers. But there are a few important conditions.
- The initial and final markers are always different.
- The initial and final markers are always 1 char size.
- The initial and final markers always exist in a string and go one after another.

Input: Three arguments. All of them are strings (str).
        The second and third arguments are the initial and final markers.
Output: A string (str).
"""


def between_markers(text: str, start: str, end: str) -> str:
    substring = []
    start_bracket = False
    empty_substring = ""
    for i in text:
        if i == start:
            start_bracket = True
        elif i == end and start:
            substring.append(empty_substring)
            empty_substring = ""
            start_bracket = False
        elif start_bracket:
            empty_substring += i
    if empty_substring:
        substring.append(empty_substring)
    return ''.join(substring)


def between_markers_2_0(text: str, start: str, end: str) -> str:
    start_marker = text.index(start)
    end_marker = text.index(end)
    substring = text[start_marker + 1:end_marker]
    return substring


if __name__ == '__main__':
    print("Example:")
    print(between_markers("What is >apple<", ">", "<"))
    print(between_markers_2_0("[an apple]", "[", "]"))
