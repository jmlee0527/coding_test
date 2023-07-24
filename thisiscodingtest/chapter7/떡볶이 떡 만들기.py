#떡볶이 떡 만들기
import sys
n,m = map(int,sys.stdin.readline().split())

ricecake = list(map(int,sys.stdin.readline().split()))
ricecake.sort()

result = 0
start = 0
end = max(ricecake)

while start <= end:
    total = 0
    mid = (start+end) //2
    for i in ricecake:
        if i > mid:
            total += i-mid
    if total < m:
        end = mid -1
    else:
        result = mid
        start = mid+1

print(result)
