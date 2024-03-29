from collections import defaultdict


def first_word(text: str) -> str:
    """
       Returns the first word of the input text that is separated by a space
    """
    if isinstance(text, str):
        strip_text = text.strip()
        index = strip_text.find(" ")
        return strip_text[:index] if index != -1 else strip_text
    else:
        raise TypeError("expected type is 'str', but actual is '{}'".format(text.__class__.__name__))


def most_frequent(data: list) -> str:
    """
       Returns the most frequent string of the input list
       In case there are strings with the same frequency, returns the string of ordered from smallest to largest data
       separated by comma
    """
    if not isinstance(data, list):
        raise TypeError("expected input type is 'list'")
    if any(not isinstance(item, str) for item in data):
        raise TypeError("expected inner list type is 'string'")
    unique_data = sorted(set(data))
    max_count = 0
    res = []
    for item in unique_data:
        current_count = data.count(item)
        if current_count > max_count:
            max_count = current_count
            res = [item]
        elif current_count == max_count:
            res.append(item)
    return ", ".join(res)


def most_frequent_with_max(data: list) -> str:
    """
       Returns the most frequent string of the input list
       In case there are strings with the same frequency, returns the first string
    """
    return max(data, key=data.count)


def most_frequent_with_dict(data: list) -> list:
    """
       Returns the most frequent strings of the input list sorted by alphabet
    """
    mydict = defaultdict(list)
    for item in set(data):
        mydict[data.count(item)].append(item)
    return sorted(mydict[max(mydict.keys())])
