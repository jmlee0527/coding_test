#1로 만들기
import sys

n = int(sys.stdin.readline())

d = [0] *35000

for i in range(2,n+1):      #bottom-up 방식
    d[i] = d[i-1] +1

    if i%2 == 0:
        d[i] = min(d[i],d[i//2]+1)
    if i%3 == 0:
        d[i] = min(d[i],d[i//3]+1)
    if i%5 == 0:
        d[i] = min(d[i],d[i//5]+1)

print(d[n])