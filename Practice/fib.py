
def fib(n):
    if n < 0:
        return "Invalid number"
    elif n == 1 or n == 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# x = fib(5)
# print(x)

n = 5
num1 = 0
num2 = 1
next_num = num2
count = 1

while count <= n:
    print(next_num, end=' ')
    count += 1
    num1, num2 = num2, next_num
    next_num = num1 + num2
print()