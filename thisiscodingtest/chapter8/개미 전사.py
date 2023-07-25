#개미 전사
import sys
n = int(sys.stdin.readline())

food = list(map(int,sys.stdin.readline().split()))

d = [0] * 1001

d[0] = food[0]
d[1] = food[1]

for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+food[i])

print(d[n-1])