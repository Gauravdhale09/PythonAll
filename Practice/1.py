n = int(input())
t = tuple(map(int, input().split()))[:n]

print(t)
print(hash(t))