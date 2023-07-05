#################################### SUPER TASK 3####################
secretNum = 7777
guess = int(input("Guess the number: "))
  
while secretNum != guess:
  print("Not correct, try again!")
  guess = int(input("Guess the number: "))
  
print("Success")

#####################################################################

# Example code 1

# Add comments to each line to say whehter it is inside or outside the loop and what it does.

# Explain the circumstances in which the loop will run.

print("What is the capital of France?")
# print function telling us what to do 
answer = input() 
# variable with input function

while answer != "paris":
# while loop for checking if the answer is Paris or not
  print("Incorrect! Try again.")
  # print function
  answer = input("What is the capital of France?")
  # getting a new string for the variable answer

print("Correct!")
# the final print function with information

# Example code 2

counter = 1
# var with an int

while counter < 5:
# while loop with boolean condition counter < 5
  print("This code is inside the loop")
  # print function
  counter += 1
  # counter += 1 will be executed as many times, as it is defined in the boolean condiition



  
  