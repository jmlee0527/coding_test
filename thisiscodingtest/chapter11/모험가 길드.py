"""
그리디 알고리즘

공포도를 오름차순으로 정렬하여 공포도가 낮은 인원부터 그룹을 정하도록 한다.
최소한의 인원으로 그룹을 결성하는 것으로 최적의 해가 된다.
"""

import sys

input = sys.stdin.readline

n = int(input())

fear = list(map(int,input().split()))

fear.sort()

result = 0

cnt = 0     #그룹 내 인원수
for i in fear:
    cnt += 1
    if cnt >= i:
        result +=1
        cnt = 0

print(result)