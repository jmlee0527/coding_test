#백준 1260번 - DFS와 BFS
"""
DFS - 깊이 우선 탐색
BFS - 너비 우선 탐색

"""
import sys
from collections import deque
n,m,v = map(int,sys.stdin.readline().split())

graph = [[0] *(n+1) for _ in range(n+1)]
for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())
    graph[i][j] = 1
    graph[j][i] = 1

d_visited = [0] * (n+1)
b_visited = [0] * (n+1)

def bfs(v):
    q = deque([v])
    b_visited[v] = 1
    while q:    #방문할 노드가 없을때까지
        v = q.popleft()
        print(v,end = " ")
        for i in range(1,n+1):
            if not b_visited[i] and graph[v][i]:    #i노드를 방문하지 않았고 현재 v와 연결되어있다면!
                q.append(i)             #다음 탐색 대상으로 추가
                b_visited[i] =1         #해당 대상은 visited로 판단 -> 이미 추가했으므로

def dfs(v):
    d_visited[v] =1
    print(v,end = " ")
    for i in range(1,n+1):
        if not d_visited[i] and graph[v][i]:
            dfs(i)          #재귀함수를 통해 계속해서 깊이 탐색
dfs(v)
print()
bfs(v)
print("")


