

# Input: Ask the user to enter a year
year = int(input("Enter a year: "))

def is_leap_year(year):
    # Correct leap year logic
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
# Output: Display whether it's a leap year or not
if is_leap_year(year):
    print("is a leap year.")
else:
    print("is not a leap year.")
