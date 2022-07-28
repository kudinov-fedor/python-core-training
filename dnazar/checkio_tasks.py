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
    if isinstance(data, list) and all(isinstance(item, str) for item in data):
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
    else:
        raise TypeError("expected type is 'list of strings'")


def most_frequent_with_max(data: list) -> str:
    """
       Returns the most frequent string of the input list
       In case there are strings with the same frequency, returns the first string
    """
    return max(data, key=data.count)
