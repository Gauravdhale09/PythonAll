a=int(input("Enter 1st number="))
b=int(input("Enter 2nd number="))
c=int(input("Enter 3rd number="))

max = (a>b) ? (a>c ? a:c) : (b>c ? b:c)
print("largest number among a,b and c")