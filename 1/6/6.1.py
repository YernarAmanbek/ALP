# Example code 1

number = 7
# variable with an integer
print("I have thought of a number between 1 and 10")
# print function with a string
guess = int(input("Can you guess what it is?: "))
# input function, so a user can input data

if guess == number:
  print("Correct!")
# if function, if guess == number, then it will give "correct!"
elif guess < number:
  print("Too Low!")
# else if guess < number, then it will give "too low!"
else:
  print("Too High!")
# if there are no other cases, it will give "too high!", but in this case if guess > number

# Example code 2

number1 = int(input("\nPlease enter a number: "))
number2 = int(input("Please enter another number: "))
# two variables with input functions, so we can compare two numbers

if number1 > number2:
  print("\n" + str(number1) + " is bigger than " + str(number2))
# if function with comparison
elif number2 > number1: 
  print(str(number2) + " is bigger than " + str(number1))
# same as the previous one
else:
  print("Both numbers are the same")
# else, they are equal
