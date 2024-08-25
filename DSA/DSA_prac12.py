# Insertion Sort

def insert(elements):
    print(f"unsorted:{elements}")
    for i in range(1, len(elements)):
        PTR = elements[i]
        j = i - 1
        while j>=0 and PTR < elements[j]:
            elements[j+1] = elements[j]
            j-=1
        elements[j+1] = PTR
        print(f"compare {PTR}:{elements}")
    print(f"sorted:{elements}")

if __name__ == '__main__':
    elements1 = [11,9,29,7,2,15,28]
    elements2 = ["gaurav", "priyal", "ankush", "anushka", "sakhi","vasudev"]
    insert(elements2)