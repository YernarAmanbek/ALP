# Starter Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))


if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")
if guess == number:
  print("exactly")

