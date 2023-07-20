#백준 1389번 - 케빈 베이컨의 6단계 법칙
"""
플로이드-워셜 알고리즘을 사용하여 풀이가 가능
"""
import sys
n,m = map(int, sys.stdin.readline().split())

graph = [[0]*n for _ in range(n)]       #0으로 2차원 배열 초기화

for _ in range(m):
    i,j = map(int,sys.stdin.readline().split())
    graph[i-1][j-1] = 1     #서로 연결되어있는 상황으로 각각 1로 설정
    graph[j-1][i-1] = 1

#플로이드-워셜 알고리즘
for k in range(n):
    for i in range(n):  #출발점
        for j in range(n):  #도착점
            if graph[i][k] and graph[k][j]:
                if graph[i][j] == 0:
                    graph[i][j] = graph[i][k] + graph[k][j]
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])       #min 값을 바로 계산

min = 10000000000000            #min값 비교를 위해 큰 값 임의로 설정
for i in range(n):
    sum = 0
    for j in range(n):
        sum += graph[i][j]
    if sum < min:
        min = sum
        person = i+1

print(person)