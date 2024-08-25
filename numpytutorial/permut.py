from itertools import permutations,combinations,combinations_with_replacement
from itertools import permutations as pts
permt = pts([2],3)
print(permt)
for i in list(permt):
    print(i)
comt = combinations_with_replacement([True , False],5)
#for i in list(comt):
    #print(i)