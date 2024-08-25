a=[]
x=int(input("Enter number of students in class="))
print("Enter name of students=")
for i in range(x):
    x=input()
    a.append(x)
m=sorted(a)
print(m)
b=[]
for i in range(728,(728+(len(m)+1))):
    b.append(f"------22BD310{i}")
print(b)
for i,j in zip(m,b):
    print(i,j)
