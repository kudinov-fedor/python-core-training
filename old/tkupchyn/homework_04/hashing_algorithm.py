from collections import defaultdict


def count_checksum(word):
    return sum(ord(letter) * (index + 1) for index, letter in enumerate(word))


def group_words_by_checksum(words_to_order, number_of_groups):
    result = defaultdict(list)

    for word in words_to_order:
        group = count_checksum(word) % number_of_groups
        result[group].append(word)

    return result
