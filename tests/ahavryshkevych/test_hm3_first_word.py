def first_word(text: str) -> str:
    word_list = []
    for i in text:
        if i != " ":
            word_list.append(i)
        else:
            break
    word = "".join(word_list)
    return word


print("Example:")
print(first_word("Hello world"))
# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
