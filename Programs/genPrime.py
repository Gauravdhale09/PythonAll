def checkPrime(c):
    prime = True
    for i in range(2, c):
        if c%i == 0:
            prime = False
            break
    return prime
def generatePrime(num):
    for i in range(2, num+1):
        if checkPrime(i):
            print(i)

if __name__ == "__main__":
    generatePrime(11)