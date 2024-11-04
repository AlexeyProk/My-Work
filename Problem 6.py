



#Input currency
amount = float(input("Enter the amount of currency: "))
if amount <= 0:
    raise ValueError ("Numbers must be positive. ")
# Convert to EUR
Euro = amount * 0.85

#Output
print("Euro", Euro)



