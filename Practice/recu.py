def pow(a,n):
    if n == 1:
        return a;
    else:
        return a * pow(a,n-1)

def main():
    res = pow(2,64);
    
    print(res)

main()