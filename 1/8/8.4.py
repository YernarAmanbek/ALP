'''
Reference Link
https://docs.google.com/document/d/1Lf221krWqB0vv5zSaQDvzBi6you6AuKdfn5x1TETh7Q/edit?usp=sharing
'''
'''
## Task Instructions - Beat The Zombie

This task requires you to combine lots of skills from earlier lessons. Don't be afraid to look at your old code, google ideas and have fun with the dialogue.  Good luck!

Write a program that simulates an encounter with a zombie in an RPG

1- Create a list of possible weapons.
2- In a variable called ‘zombieWeakness’ store the name of one of the weapons from the list.
3- Output messages telling the user that they have encountered a zombie and should prepare to fight.
4- Output the list of weapons to the user.  Ask if they want to type 1 to use one from the list or 2 to pick their own.  
  4.1- If they type 1 then they should input the weapon name - store it to a new variable. 
  4.2- If they type 2 they should input the weapon name - add it to the list and save it to a new variable.
5- If the weapon picked matches the zombieWeakness, output a message telling the user that they have won the fight.  
  5.1- Otherwise output a message saying that they have lost.

'''

weapons = ['banana', 'apple', 'rifle', 'iphone', 'coin']

zombieWeakness = weapons[1]

print("There is a zombie, be ready")
print("Here is the list of weapons: " + str(weapons))


while True:
  try:
    choice = int(input("\nDo you want to choose a weapon from this list, or pick your own (type 1 or 2 respectively): "))

    if choice != 1 and 2:
      print("\ntype 1 or 2")
    
    if choice == 1:
      weaponChoice = input("Enter what you want: ")
      weaponChoice2 = weaponChoice.lower()
      if weaponChoice2 == zombieWeakness:
        print("\n----------------------You won-------------------------")
      else: 
        print("\n----------------------You lost------------------------")
    elif choice == 2:
      weaponInput = input("Enter the name of your weapon: ")
      weaponInput2 = weaponInput.lower()
      if weaponInput2 != weapons:
        weapons.append(weaponInput2)
        print("\nYour weapon has been added to the list")
      elif weaponInput2 == weapons:
        print("\nYour weapon is already in the list")
        
      if weaponInput2 == zombieWeakness:
        print("You won")
      else: 
        print("\n----------------------You lost------------------------")
    else:
      print("\n-----------------------------Error-3000---------------------------")
  except ValueError:
    print("Try again")