# Example Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")

# What happens if you input the guess '2'?
  # Answer: if a user inputs "guess" 2, then it will give the result "corect", if it is larger than 2, Too High, and if its 1, then it will give us too low!

# What happens if you input the guess '6'?
  # Answer: if input == 6, then it will give correct!
  # if 1 =< input < 6, then it will give too low
  # if 6 < input =< 10, then it will give too high

# What happens if you input the guess '5'?   
  # Answer: if input == 5, then it will give correct!
  # if 1 =< input < 5, then it will give too low
  # if 5 < input =< 10, then it will give too high


# What happens if you input the guess '-5'?
  # Answer: It would still work, as we defined if function to give defined answers in different cases, but the thing is that a user might not know, that the answer is -5, as we gave the insctruction to choose between 1 and 10

# What happens if you input the guess '0'?
  # Answer: if input == 0, then it will give correct!
  # if -infinity =< input < 0, then it will give too low
  # if 0 < input =< infinity, then it will give too high

# What do the symbols '<' and '>' mean on lines 9 and 11?
  # Answer: guess < number; means that the number that was guessed by the user is lower than the actual number, and reversely for the > sign.

# What happens if you change line 5 to if guess = number: ?
  # Answer: if guess == number:
            #print("Correct!")
          # In this case it doesnt make sense, it will give an error. Invalid syntax

# What do you notice about each line that FOLLOWS each IF statement?
  # Answer: variable | or statement that is supposed to be executed/satisfied


