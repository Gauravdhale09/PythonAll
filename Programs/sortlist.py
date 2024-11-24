

def sortlist(list):
    for i in range(len(list)):
        for j in range(0, len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

numbers = [5, 3, 8, 1, 9, 7]
sorted_numbers = sortlist(numbers)
print(sorted_numbers)