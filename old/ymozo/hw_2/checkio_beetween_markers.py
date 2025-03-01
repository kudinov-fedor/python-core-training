def between_markers(text: str, start: str, end: str) -> str:
    start_marker = text.find(start) + len(start)
    end_market = text.find(end)
    final_string = text[start_marker:end_market]
    return final_string


if __name__ == '__main__':
    print("Example:")
    print(between_markers("What is >apple<", ">", "<"))

    # These "asserts" are used for self-checking
    assert between_markers("What is >apple<", ">", "<") == "apple"
    assert between_markers("What is [apple]", "[", "]") == "apple"
    assert between_markers("What is ><", ">", "<") == ""
    assert between_markers("[an apple]", "[", "]") == "an apple"

    print("The mission is done! Click 'Check Solution' to earn rewards!")