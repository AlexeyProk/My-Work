


#input
weight_input = input("Enter your weight in Kilograms: ")
height_input = input("Enter your height in meters: ")

#conver input
weight = float(weight_input)
height = float(height_input)

#processing
bmi = weight / (height ** 2)

#output
print("Your BMI is:", bmi)

