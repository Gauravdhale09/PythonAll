# insertion sort

def merge_sorted_two(arr1, arr2):

    sorted = []
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)

    i = 0
    j = 0
    while 1 < len_arr1 and j < len_arr2:
        if arr1[i] <= arr2[j]:
            sorted.append(arr1[i])
            i = i + 1
        else:
            sorted.append(arr2[j])
            j = j+ 1

    while i < len_arr1:
        sorted.append(arr1[i])
        i = i + 1
    while j < len_arr2:
        sorted.append(arr2[j])
        j = j + 1
    print(sorted)
    return sorted

# selection sort
# def min(arr):
#     mini = 100000000
#     for i in range(len(arr)):
#         if arr[i] < mini:
#             mini = arr[i]
#     print(mini)
#     return mini
def select(arr):

    size = len(arr)
    for i in range(size):
        min_i = i
        for j in range(min_i+1,size):
            if arr[j] < arr[min_i]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]

    print(arr)


if __name__ == '__main__':
    a = [5,8,12,56,2,3]
    b = [7,9,45,51]


    select(a)
