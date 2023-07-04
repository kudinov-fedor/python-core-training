"""
**********************************************************************
Three Words

Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters.
You should check if the string contains three words in succession. For example, the string "start 5 one two three 7 end"
contains three words in succession.
**********************************************************************
"""


def checkio(words: str) -> bool:

    # edge cases
    words_list = words.split()
    list_size = len(words_list)
    if list_size < 3:
        return False

    # final steps
    for i in range(0, list_size - 1):
        if i <= list_size - 3:

            is_all_alpha = all(map(str.isalpha, words_list[i: i + 3]))

            if not is_all_alpha:
                continue

        return is_all_alpha
