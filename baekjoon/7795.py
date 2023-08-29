#백준 7795번 - 먹을 것인가 먹힐 것인가
"""
n,m 개수가 20000개로 하나씩 비교하는 경우 시간초과가 발생한다.
이진탐색을 이용하여 시간복잡도를 줄여서 문제를 해결한다.
"""
import sys
input = sys.stdin.readline
    
def binary_search(array,target):
    start = 0
    tmp = -1
    end = len(array)-1
    while start <= end:
        mid = (start+end) //2
        if array[mid] < target:
            tmp = mid
            start = mid +1
        else:
            end = mid -1
    return tmp

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    cnt = 0
    for i in a:
        cnt += (binary_search(b,i) + 1)
    print(cnt)
