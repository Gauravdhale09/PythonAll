# Bubble sort

def bubble(elements):
    size = len(elements)
    print("unsorted list:",elements)
    for k in range(size-1):
        for i in range(size-1):
            if elements[i] > elements[i+1]:
                t = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = t
        print(f"pass{k+1}: {elements}")
    print("Finally sorted=", elements)

# Quick sort

def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp
def part(elements,srt,end):

    p_index = srt
    pivot = elements[p_index]


    while srt < end:
        while srt<len(elements) and elements[srt] <= pivot:
            srt+=1
        while elements[end] > pivot:
            end-=1

        if srt < end:
            swap(srt, end, elements)
    swap(p_index, end, elements)
    return end
def quick(elements,srt,end):
    #first step we have to do is for partition
    if srt < end:
        partition_index = part(elements, srt, end)
        quick(elements, srt, partition_index - 1)  # left partition
        quick(elements, partition_index + 1, end)  # right partition


if __name__ == '__main__':
    elements1 = [11,9,29,7,2,15,28]
    elements2 = ["gaurav", "priyal", "ankush", "anushka", "sakshi","vasudev"]
    quick(elements2,0,len(elements2)-1)
    print(elements2)




