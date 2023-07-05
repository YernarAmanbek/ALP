failGrade = 40
# variable failGrade stands for the test grade, when you have to retake

print("-----------------------------------------------------------------")
print("---------------------GRADE-CALCULATOR-8000-----------------------")
print("-----------------------------------------------------------------")
print("\nType '1234' if you want to close")

while True:
  try:
    grade = int(input("\nInput your test grade: "))
    # input variable
  
    fail = ""
    # empty string variable fail
  
    if 1 <= grade <= failGrade:
      fail = "Y"
    elif grade >= failGrade:
      fail = "N"
    # Simple if/else function to assign Y or N to the variable fail
  
    if fail == "Y":
      print("Retake required")
    # function checks if you have to retake or not
  
    if 1 <= grade < failGrade:
      print("Grade 'U'")
    elif 40 <= grade <= 68:
      print("Grade 'C'")
    elif 69 <= grade <= 79:
      print("Grade 'B'")
    elif 80 < grade <= 100:
      print("Grade 'A'")
    elif grade == 1234:
      print("\n-----------------------------------------------------------------")
      print("---------------------------GOOD-BYE------------------------------")
      print("-----------------------------------------------------------------")
      break
    # to close the application
    elif grade == 0000:
      print("\n*Knock* *Knock* \n'Who is there? \n*Silence*'")
    # Humoristic line
    elif grade == 7777:
      print("\nYeye")
  
    else:
      print("That is not a grade")
    # Extra Challange part for the grading
  except ValueError:
    print("\n------------------------------")
    print("-WE NEED POSITIVE INTEGERS!!!-")
    print("------------------------------")