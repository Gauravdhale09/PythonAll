# #no argument no result
# def add():
#     a=int(input("Enter number="))
#     b=int(input("Enter number="))
#     c=a+b
#     print("add=",c)
# add()
# #with argument no result
# def sub(a,b):
#     c=a-b
#     print(c)
# a=int(input("Enter number="))
# b=int(input("Enter number="))
# sub(a,b)
# #with argument no result
# def mul(a,b):
#     c=a*b
#     print(c)
# a = int(input("Enter number="))
# b = int(input("Enter number="))
# mul(a,b)
# #with argument with result
# def div(a,b):
#     c=a/b
#     return c
# a=int(input("Enter number="))
# b=int(input("Enter number="))
# z=div(a,b)
# print(z)
i=0
while i<=5:
    i=i+1
    if i==3:
        continue
    print(i)
i=0
while i<=5:
    i=i+1
    if i==3:
        break
    print(i)