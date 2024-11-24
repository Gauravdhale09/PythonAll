
def armstrong(num):
    sum = 0
    for i in str(num):
        sum += int(i) ** len(str(num))
    return sum == num

print(armstrong(15))