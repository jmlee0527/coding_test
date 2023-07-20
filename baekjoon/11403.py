#백준 11403번 - 경로 찾기
"""
플로이드-워셜 알고리즘을 이용하면 보다 쉽게 이해하고 풀이가 가능하다.
플로이드-워셜 알고리즘 -> 모든 경로에 대한 정점을 계산하는 알고리즘
"""
import sys
n = int(sys.stdin.readline())

graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

#플로이드-워셜 알고리즘
for k in range(n):          #모든 정점 확인을 위한 변수 k , i에서 j로 경로를 k를 통해 확인
    for i in range(n):        
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1         #경로가 있는 경우 1로 저장

for i in range(n):
    print(*graph[i])



