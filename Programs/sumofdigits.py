
def sumofdigits(digit):
    sum = 0
    for i in range(len(str(digit))):
        sum += int(i)
    return sum

print(sumofdigits(10))
