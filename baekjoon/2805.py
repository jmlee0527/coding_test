#백준 2805번 - 나무 자르기
"""
이분 탐색 방법을 통해 나무를 가져가기 위한 절단 높이를 빠르게 탐색한다.
"""
import sys
n,m = map(int,sys.stdin.readline().split())

high = list(map(int,sys.stdin.readline().split()))     #나무들의 높이를 리스트에 저장한다.

high.sort()
start = 0
end = high[-1]       #나무의 최대 높이를 end값으로 설정한다.
result = 0
while start <= end:
    tree = 0            #자르고 남은 나무들의 합을 tree 변수에 저장한다.
    mid = (start+end)//2        
    for i in high:          #절단 높이가 mid 일때 가져갈 수 있는 나무의 합을 구한다.
        if mid < i:
            tree += (i-mid)
    if tree >= m:      #나무의 합이 m보다 큰 경우 나무의 절단 높이를 높은범위로 옮긴다.
        start = mid+1
    else :      #나무의 합이 m보다 작은 경우 나무의 절단 높이를 낮은범위로 옮긴다.
        end = mid-1

print(end)


