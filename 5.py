string = "Practice Problems to Drill List Comprehension in Your Head."
letters = string.split()
Letters = [letter for letter in letters if len(letter) < 5]
print("The words in the string that are less than 5 letters: ", end="")
print(Letters)
