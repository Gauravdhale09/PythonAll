# a=[]
# m=int(input("val="))
# for i in range(1,m+1):
#     a.append(i)
# mul = 1
# print(a)
# mul = 1
# for j in a:
#     mul = j * mul
# print(mul)

def fact(a):
    if a <= 1:
        return 1
    else:
        return a*fact(a-1)

print(fact(5))

def fibonacci(a):
    if a < 0:
        return "Incorrect number"
    elif a==0:
        return 0
    elif a==1 or a==2:
        return 1
    else:
        return fibonacci(a-1) + fibonacci(a-2)

print(fibonacci(4))