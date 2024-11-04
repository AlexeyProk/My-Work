



#input/Prepare user to enter their age
age_input = input("Pleas enter your age: ")

# Check if the inout is a number and not an empty string
if age_input.isdigit():
    age = int(age_input)
    # Ensure the age is positive
    if age > 0:
        #Classify the age into categories
        if age < 18:
            print("Minor")
        elif 18 <= age <= 65:
            print("Adult")
        else:
            print("senior citizen")
    else:
        print("Error: Age must be a positive number. ")
else:
    print("Error: invalid input. Please enter a positive integer. ")