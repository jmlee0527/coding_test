#부품 찾기

#1. 라이브러리 사용
import sys

n = int(sys.stdin.readline())
store = list(map(int,sys.stdin.readline().split()))
store.sort()

m = int(sys.stdin.readline())
check = list(map(int,sys.stdin.readline().split()))

for i in range(m):
    if check[i] in store:
        print("yes", end = " ")
    else:
        print("no", end = " ")

print()

#2. 이진 탐색 - 반복문
import sys

n = int(sys.stdin.readline())
store = list(map(int,sys.stdin.readline().split()))
store.sort()

m = int(sys.stdin.readline())
check = list(map(int,sys.stdin.readline().split()))

def binary_search(array,start,end,target):
    while start <= end:
        mid = (start+end) //2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return None

for i in range(m):
    target = check[i]
    result = binary_search(store,0,len(store),target)
    if result == 1:
        print("yes", end = " ")
    else:
        print("no", end = " ")

print()
