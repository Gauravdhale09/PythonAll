
def countvowels(strings):
    checklist = []
    check = 'AEIOUaeiou'
    for i in range(len(strings)):
        for char in check:
            if strings[i] == char:
                checklist.append(strings[i])
    return checklist

                
            
x = "GaUrAv"
print(countvowels(x))

            