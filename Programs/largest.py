
def large(list):
    size = len(list)
    if size == 0:
        return None
    max_val = list[0]
    for i in range(1, size):
        if list[i] > max_val:
            max_val = list[i]
    return max_val
lst = [425566, 12, 13, 14, 525, 15, 16, 17]
result = large(lst)
print(f"The largest number in the list is: {result}")