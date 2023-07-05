# Starter code

num1 = 10
num2 = int(input("What number you want to choose?: "))
# because the input given by the user is always defines as a string, we have to use int() function to convert str to int

total1 = num1 + num2

print(str(num1) + " plus " + str(num2) + " = " + str(total1))
# since the print function uses string " plus ", we have to convert total1 to string format

total2 = num1 * num2
print(str(num1) + " multiplied by " + str(num2) + " = " + str(total2))

# Instructions

# Line 4 creates an error. Look carefully to see what is wrong with the code and fix it.

# Add a text prompt between lines 3 and 4 to tell the user to enter a number.

# Complete line 8 to concatenate total 1 into the output statement.

# Add a new variable with a sensible identifier.  Multiply num1 and num2 together and assign the result into this variable.

# Output num1, num2 and your new variable in a similar format to line 8.