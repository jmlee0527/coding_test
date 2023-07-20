#백준 1920번 - 수 찾기
"""
특정값을 찾아내는 문제에서는 이분탐색을 사용하는 것이 효율적이다.
이분탐색의 기본 전제 조건은 정렬이 되어있어야 한다.

"""
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m= int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

a.sort()        #이분탐색의 전제 -> 정렬
for i in target:
    start = 0
    end = len(a)-1
    while start <= end:         #start,mid,end를 설정하여 이분탐색으로 확인
        mid = (start + end) //2
        if i > a[end] or i<a[start]:
            print(0)
            break
        elif i == a[mid]:
            print(1)
            break
        elif i < a[mid]:
            end = mid -1
        elif i > a[mid]:
            start = mid+1


