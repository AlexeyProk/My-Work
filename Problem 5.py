



#Input time in hours

hours = float(input("Enter the time in hours: "))

# non negative
if hours <= 0:
    raise ValueError ("Numbers must be positive.")

# calculate minutes and seconds
minutes = hours * 60
seconds = minutes * 60

#output for area
print("minutes is: ", minutes)
print("seconds is", seconds)