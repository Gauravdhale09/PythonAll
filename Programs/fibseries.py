
def fib(x):
    a, b = 0,1
    sum = 0
    for _ in range(x):
        print(a, end=' ')
        sum += a
        a, b = b, a + b
    return sum
s = fib(5)
print("sum = ", s)