



#Input for 2 different variables

lenght = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# length and width entered by the user are positive numbers
if lenght <= 0 or width <=0:
    raise ValueError ("Numbers must be positive.")

#area calculator
area = lenght * width

#output for area
print("area is: ", area)