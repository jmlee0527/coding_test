"""

"""
n,m = map(int,input().split())

pound = list(map(int,input().split()))

pound.sort()

result = 0

for i in range(n):
    for j in range(i+1,n):
        if pound[i] != pound[j]:
            result += 1
print(result)