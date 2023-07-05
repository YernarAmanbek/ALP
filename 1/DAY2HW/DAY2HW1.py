'''
Task Instructions
You are going to write a program called "Time Reminder"

The user has to enter a number between 0 and 23
If the number is less than 8 display a message saying "too early to get up"
If the number is less than 12 display a message saying "Good morning"
If the number is less than 14 display a message saying "Lunch time!"
If the number is less than 18 display a message saying "Good afternoon"
If the number is equal to 18 display a message saying "Tea Time"
If the number is less than 19 display a message saying "Good evening"
If the number is less than 22 display a message saying "Nearly bedtime"
If the number is 23 display a message saying "Good night!"
Any other number is met with the response “Sorry, I don’t recognise that”


You are free to use any of the methods that we have learned in class.
'''
#Start coding below this line

number = int(input("Input number: "))

if number < 8:
  print("too early to get up")
elif 8 <= number < 12:
  print("Good morning")
elif 12 <= number < 14:
  print("Lunch time")
elif 14 <= number < 18:
  print("good afternoon")
elif 18 == number:
  print("tea time")
elif 18 < number < 19:
  print("good evening")
elif 19 <= number < 22:
  print("nearly bedtime")
elif 22 <= number <= 23:
  print("good night")
else:
  print("sorry i dont recignize that")