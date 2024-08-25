n = input("Enter type of operation=")
list = ["Addition" , "Subtraction" , "Multiplication" , "Division"]

if n==list[0]:
    a=int(input("Enter value of a="))
    b = int(input("Enter value of b="))
    c= a+b
    print("Addition=",c)
elif n==list[1]:
    a=int(input("Enter value of a="))
    b = int(input("Enter value of b="))
    c = a - b
    print("Subtraction=", c)
elif n==list[2]:
    a = int(input("Enter value of a="))
    b = int(input("Enter value of b="))
    c = a * b
    print("Multiplication=", c)
elif n==list[3]:
    a = int(input("Enter value of a="))
    b = int(input("Enter value of b="))
    c = a / b
    print("divion=", c)
else:
    print("error")