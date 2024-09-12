
def Solution(l1, l2):
    l1.reverse()
    l2.reverse()
    int1 = str(l1).replace(',', '').replace('[', '').replace(']', '').replace(' ','')
    int2 = str(l2).replace(',', '').replace('[', '').replace(']', '').replace(' ','')
    print(int1, int2)
    print(int(int1) + int(int2))

    
l1 = [1,5,6]
l2 = [5,7,8]
Solution(l1,l2)