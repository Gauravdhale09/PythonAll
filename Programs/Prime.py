def FindPrime(n):
    prime = True
    for i in range(2, n):
        if n%i == 0:
            prime = False
            break

    print(prime)

if __name__ == '__main__':
    FindPrime(8)
