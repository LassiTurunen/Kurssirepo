#Make a Python program, which prompts for a compound word.

#Get following aspects from the word
#Length
#First character
#Reversed version e.g. “Suitcase” is reversed “esactiuS”
#Display the aspects using print commands.
#Prompt the user to take substring from the existing compound word.
#Finally print the user specified substring.

print("Program starting.\n")
word = input("Insert a closed compound word: ")
reverse = word[::-1]

print(f"The word you inserted is '{word}' and in reverse it is '{reverse}'.")

length = (len(word))
print(f"The inserted word length is {length}")

last = word[-1]
print(f"Last character is '{last}'\n")

print("Take substring from the inserted word by inserting...")
one = int(input("1) Starting point: "))
two = int(input("2) Ending point: "))
three = int(input("3) Step size: "))
complete = word[one:two:three]

print(f"\nThe word '{word}' sliced to the defined substring is '{complete}'.")
print("Program ending.")