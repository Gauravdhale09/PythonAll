maxof = lambda x, y: x if x>y else y
add = lambda x, y: x+y
a,b = [int(x) for x in input("enter two numbers: ").split(',')]

print(f"max={maxof(a,b)}")
print("addition of {} and {} is {}".format(a, b, add(a, b)))
