while True:
  try:
    num1 = int(input("First Nomber: "))
    num2 = int(input("Secand Nomber: "))
    
    def add(num1,num2):
       return num1+num2
      
    def substract(num1,num2):
      return num1-num2
    
    def multiply(num1,num2):
      return num1*num2
    
    def divide(num1,num2):
      return num1/num2
    
    operation = int(input("what math iperation you want? (1-add, 2-substract, 3-multiply, 4-divide): "))
    
    if operation == 1:
      print(str(add(num1,num2)) + " is the resolt")
    elif operation == 2:
      print(str(substract(num1,num2)) + " is the resolt")
    elif operation == 3:
      print(str(multiply(num1,num2)) + " is the resolt")
    elif operation == 4:
      print(str(divide(num1,num2)) + " is the resolt")
    else:
      print("WHOT?")
    break
  except ValueError:
    print("WE NEED NOMBERS")