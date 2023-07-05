# Program to calculate the area of a rectangle

# Get input for height & width. Convert to integers and store in variables

# Calculate the area & store the result in the area variable

# Output the area variable (converted to string)

width = int(input("width?: "))
height = int(input("height?: "))
area = width * height
print(str(area))








'''
Extra Challenges
Perimeter Calc
Create a program that allows the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the perimeter of the rectangle. 
Restaurant Tip Calculator 
Create a program that allows the user to enter the price of a meal at a restaurant. The program calculates the amount of the tip to be paid at 20%. The tip and total price are then displayed separately.
Volume and Surface Calc 
Create a program that allows the user to enter 3 numbers representing the height, width and length of a cuboid. The program calculates and displays the volume and total surface area of the cuboid. 
'''

# Perimeter Calc
print("\n----------------------------------")
print("--------Perimeter-calculator------")
print("----------------------------------")

widthPer = int(input("Input width: "))
heightPer = int(input("Input height: "))
print(str( 2 * (widthPer + heightPer)) + " is the perimeter")

# Tip Calculator
print("\n----------------------------------")
print("--------Restaurant-Helper---------")
print("----------------------------------")
foodPrice = int(input("Input the price for the meal: "))
tip = (foodPrice * 20) / 100
print("The price fo the meal is " + str(foodPrice) + " and the amount of tip is " + str(tip))

#Volume andSurface Calc
print("\n----------------------------------")
print("-------VOLUME-CALCULATOR-3000-----")
print("----------------------------------")
name = input("Hello, What is your name?: ")
print("Nice to meet you, " + name + "! To calculate the volume and surface of the cuboid, enter the data below!")
heightCub = int(input("Input height: "))
widthCub = int(input("Input width: "))
lenghtCub = int(input("Input lenght: "))
print("The volume is " + str(heightCub*widthCub*lenghtCub) + " and the surface area is " + str( 2*(heightCub*widthCub) + 2*(heightCub*lenghtCub) + 2*(widthCub*lenghtCub) )) 

print("\n Good Bye!")