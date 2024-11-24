# find duplicates in a list

def dup(x):
    duplicates = []
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] == x[j] and x[i] not in duplicates:
                duplicates.append(x[i])
    return duplicates
# Example usage
numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10]
duplicates = dup(numbers)
print("Duplicates:", duplicates)