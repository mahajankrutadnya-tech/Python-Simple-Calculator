# SIMPLE CALCULATOR USING PYTHON

print("==== SIMPLE CALCULATOR ====")
print("+ : Addition")
print("- : Subtraction")
print("* : Multiplication")
print("/ : Division")
print("% : Modulus")

try:
    user_no1=int(input("Enter the 1st number :"))
    user_no2=int(input("Enter the 2nd number :"))

    user_operation=input("Enter operation(+,-,/,*,%):")

    if user_operation=="+":
       print( "Result =", user_no1 + user_no2)
     
    elif user_operation=="-":
       print("Result =", user_no1-user_no2)

    elif user_operation=="/":
       if user_no2==0:
          print("Division by zero is not allowed.")
       else:
          print("Result =", user_no1 / user_no2)

    elif user_operation=="*":
       print("Result =", user_no1 * user_no2)

    elif user_operation=="%":
       if user_no2==0:
          print("Division by zero is not allowed.")
       else:
          print("Result =", user_no1 % user_no2)

    else:
      print("Invalid operation. Please choose +,-,*,/,%")

except ValueError:
   print("Please enter valid numbers only:")