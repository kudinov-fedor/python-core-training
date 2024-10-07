def get_most_wanted_letter(text: str) -> str:
    """
        Find most used letter

        Args:
            text (str): text to analyze letters usage

        Returns:
            str: letter which is used the most
    """
    text = text.lower()
    letters_dict = {}

    # count letters and store them in dictionary
    for letter in text:
        if letter.isalpha():
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1

    # calculate letter max occurrence
    max_value = max(letters_dict.values())
    # find all max values and sort their keys alphabetically
    res = sorted([key for key in letters_dict if letters_dict[key] == max_value])
    return res[0]
