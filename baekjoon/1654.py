#백준 1654번 - 랜선 자르기
"""
가장 긴 길이를 구하는 것이 목적이므로 total == n일 때 종료하면 가장 긴 길이를 출력하지 않을 수 있다.
최소길이, 최대길이를 기준으로 이분탐색을 진행하여 값을 구한다.

"""
import sys

k,n = map(int,sys.stdin.readline().split())

a = []
for _ in range(k):
    length = int(sys.stdin.readline())
    a.append(length)

start = 1       #최소 길이를 1로 설정
end = max(a)       #최대 길이는 입력 받은 값 중 가장 큰 길이로 설정
while start <= end:         #이분탐색 과정
    mid = (start+end) //2
    total = 0
    for i in a:
        total += i//mid         #mid 값으로 나누었을 때 개수를 확인
    if total >= n:        
        start = mid+1
    else:
        end = mid -1

print(end)          #end 값이 가장 긴 길이값이 된다