# guess word

word = "clever"
guesses = ["c", "l", "e"]

# display
print("".join(i if i in guesses else "_" for i in word))


# --------------------------------
# act
guesses.append("v")
# display
print("".join(i if i in guesses else "_" for i in word))
# if end check
print(set(guesses).issuperset(word))


# --------------------------------
# act
guesses.append("v")
# display
print("".join(i if i in guesses else "_" for i in word))
# if end check
print(set(guesses).issuperset(word))
