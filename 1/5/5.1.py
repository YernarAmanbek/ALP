# Example code 1

age = 18 
 
if age > 18: 
 print("You are old enough to drive") 
  # we got nothing as the if function is not satisfied.

# Example code 2

num1 = 1337 
 
if num1 == 10: 
  print("This text is output because the condition was true") 
else:
  print("This text is output because the condition was false") 
# num1 is not 10, so the function print gives out the string that says its false

# Example code 3

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))
# input assigns integer to the variable guess

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")
# if inputed integer is equals to the variable number, then print will be executed, saying its Correct!
# if inputed integer is lower to the variable number, then print will be executed, saying its Too Low!
# if inputed integer is larger to the variable number, then print will be executed, saying its Too High!