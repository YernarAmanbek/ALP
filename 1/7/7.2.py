number = 7
print("I'm thinking of a number, can you guess it?")
guess = int(input())
while guess != number:
  print("Wrong! Guess again!")
  guess = input()
print("You guessed it!")

# Give the line number where iteration starts.
  # Answer: line 4

# What does '!=' mean?
  # Answer: not equal to

# How many variables are there in the code?
  # Answer: 2

# How can you tell which lines of code are inside the loop?
  # Answer: under while loop

# How many times will the loop repeat?
  # Answer: infinitely many times, unless the condition is satisfies

# What has to happen to make the program run the last line of code?
  # Answer: the condiiton is supposed to satisfies in while loop.

#################################### SUPER TASK 3####################
  secretNum = 7777
  guess = int(input("Guess the number: "))
  
  while secretNum != guess:
      print("Not correct, try again!")
      guess = int(input("Guess the number: "))
  
  print("Success")

#####################################################################