


# Prompt the user to enter a single character
char_input = input("Please enter a single character: ")

# Check if the input is exactly one character long and is a letter
if len(char_input) == 1 and char_input.isalpha():
    # Convert the character to a lowercase
    char = char_input.lower()
    if char in "aeiou":
        print("The character before execution: ", char)
        print("The character is vowel")
    else:
        print("The character is a consonant")
else:
    # handle cases where input is not a sigle letter
    if len(char_input) != 1:
        print("Error: Please enter only one character. ")
    else:
        print("Error: The input is not a letter")