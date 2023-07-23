#두 배열의 원소 교체
import sys

n,k = map(int,sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

for i in range(k):
    a[a.index(min(a))], b[b.index(max(b))] = b[b.index(max(b))], a[a.index(min(a))]

print(sum(a))