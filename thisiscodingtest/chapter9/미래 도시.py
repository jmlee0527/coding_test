import sys
input = sys.stdin.readline

n,m = map(int,input().split())
INF = (1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x,k = map(int,input().split())

#플로이드 워셜 알고리즘 사용
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

distance = graph[1][k] + graph[k][x]
if distance == INF:
    print(-1)
else:
    print(distance)
