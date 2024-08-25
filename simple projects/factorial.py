a=[]
m=int(input("val="))
for i in range(1,m+1):
    a.append(i)
mul = 1
print(a)
mul = 1
for j in a:
    mul = j * mul
print(mul)