

#Challenge: Implement error handling to ensure that the user enters valid marks
# (between 0 and 100) for each subject.
#Input: Ask the user to enter their marks for three subjects.
#Processing: Calculate the average of the marks.
# Determine the grade based on the average:
#90 and above: A
#80-89: B
#70-79: C
#60-69: D
#Below 60: F
#Output: Display the calculated grade.

grade_input = input("Enter your grade: ")

# Check if the inout is a number and not an empty string
if grade_input.isdigit():
    grade = int(grade_input)
    # Ensure the age is positive
    if grade > 0:
        #Classify the age into categories
        if grade >= 90:
            print("Grade A")
        elif 89 >= grade >= 80:
            print("B")
        elif 79 >= grade >= 70:
            print ("C")
        elif 69 >= grade >= 60:
            print ("D")
        else:
            print("F")
    else:
        print("Error: Grade must be a positive number. ")
else:
    print("Error: invalid input. Please enter a positive integer. ")