


#input
x1 = float(input("Enter x1 coordinate"))
y1 = float(input("Enter y1 coordinate"))
x2 = float(input("Enter x2 coordinate"))
y2 = float(input("Enter y2 coordinate"))

#procccessing
x_squared = (x2 - x1) ** 2
y_squared = (y2 - y1) ** 2

distance_squared = x_squared + y_squared
distance = distance_squared ** 0.5

#output
print("This distance between points is: ", distance)



