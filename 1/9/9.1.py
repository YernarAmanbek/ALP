# Example Code 1

def say_hi():
  print("Why hello there!")
# subroutine with the print function 

def offer_drink():
  print("Would you care for a spot of tea?")
# subroutine with the print function 

def offer_food():
  print("Biscuit?")
# subroutine with the print function 

def say_bye():
  print("Cheerio then.")
# subroutine with the print function 

offer_drink()
# calling the subroutine, so it will initiate the print function
say_hi()
# calling the subroutine, so it will initiate the print function
offer_food()
# calling the subroutine, so it will initiate the print function


# Example code 2
def maths1():
  num1 = 50
  num2 = 5
  return num1 + num2
# subroutine that will return value of num1+num2, basically 55

def maths2():
  num1 = 50
  num2 = 5
  return num1 - num2
# same as the previous one, but will return 45

def maths3():
  num1 = 50
  num2 = 5
  return num1 * num2
# same as the previous subroutine, will return 250

outputNum = maths2()
# variable that calls the math2 subroutine, in the end, it will assign value 45 to the variable
print(outputNum)
# prints 45

# Example Code 3
def location(country):
  print("I am from " + country)
# subroutine with an argument

location("Brazil")
# calling the subroutine that also passes an argument to the subroutine

