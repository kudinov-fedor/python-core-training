# guess word

word = "clever"
guesses = ["c", "l", "e"]
print("".join(i if i in guesses else "_" for i in word))


guesses.append("v")                                        # act
print(set(guesses).issuperset(word))                       # if end
print("".join(i if i in guesses else "_" for i in word))   # show state


guesses.append("r")
print(set(guesses).issuperset(word))
print("".join(i if i in guesses else "_" for i in word))
