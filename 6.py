string = "Practice Problems to Drill List Comprehension in Your Head."
letters = string.split()
length = [len(letter) for letter in letters]
print("The length of each word in a sentence: ")
print(length)
