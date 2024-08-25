# Recursion technique

# simple example for recursion is of factorial

def fact(n):
    mul = 1
    for i in range(1, n+1):
        mul = mul * i
    return mul
fact(0)

def sum(n):
    s = 0
    for i in range(1, n+1):
        s = +i
    return s
sum(0)

def fin_s(n):
    if n==1:
        return 1
    return n + fin_s(n-1)
def fin_f(n):
    if n == 1 or n == 0:
        return 1
    return n * fin_s(n-1)

# recursion in fibonacci series
def fin_fi(n):
    if n==0 or n==1:
        return n
    else:
        return fin_fi(n-1) + fin_fi(n-2)
if __name__ == '__main__':
    print(fin_s(4))
    print(fin_fi(10))
    print(fin_f(4))