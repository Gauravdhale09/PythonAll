
lst = [10, 23, 25, 30, 40, 50, 60, 70]
lst1 = tuple(filter(lambda x : (x%2==0), lst))
print(lst1)