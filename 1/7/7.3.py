'''
In the modify tasks, you are given some starter code. Use the instructions below to make changes to the code. Comment your changes to explain what you have done.

Run the program to see how it works.
Adapt the code to:

1. Get user input into the number variable.
2. Change the print statement so it outputs 'number' multiplied by 'counter' equals 'product'
3. Make the counter increase by 2 every loop
4. Add a line once the loop has finished to output 'The loop has finished' '''

###################### TASK 3 B ###########################

counter = 1

numberbumber = int(input("enter a number: "))

for i in range(1,13):
  print(str(counter) + " times " + str(numberbumber) + " is " + str(counter * numberbumber))
  counter += 1  

#########################################################
counter = 1

number = int(input("Enter number: "))

while counter < 13:
  print(str(number) + " multiplied by " + str(counter) + " equals " + str(number * counter))
  counter = counter + 2

print("The loop has finished")