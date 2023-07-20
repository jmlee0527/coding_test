#백준 16439번 - 치킨치킨치킨
"""
모든 경우에 대해서 탐색하여 최대값을 구하는 완전 탐색 기법을 사용한다.
"""
import sys
from itertools import combinations

n, m = map(int,sys.stdin.readline().split())

chicken = []        #각 학생의 치킨에 대한 선호도를 2차원 배열로 저장
for _ in range(n):
    type = list(map(int,sys.stdin.readline().split()))      
    chicken.append(type)

comb = list(combinations(range(m), 3))      #치킨 종류 3가지를 구하는 모든 경우

result = []

for i,j,k in comb:      #3가지 종류 치킨에 따른 전체 만족도 합을 계산(모든 경우에 대해 탐색)
    priority = 0
    for l in range(n):
        priority += max(chicken[l][i],chicken[l][j],chicken[l][k])      #3종류 중 선호도의 최댓값을 선택하여 저장
        result.append(priority) 

print(max(result))