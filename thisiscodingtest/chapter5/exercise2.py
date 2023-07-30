#미로 탈출
"""
최소 칸의 개수를 구하기 위해 BFS 알고리즘을 활용한다 -> 탐색이 먼저 끝난 것이 최단거리이므로
"""
from collections import deque

#입력부분
n,m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

#이동할 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#BFS
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):      #상하좌우 이동하는 4가지 경우
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny<0 or nx>=n or ny>=m:        #공간을 벗어난 경우 무시
                continue
            if graph[nx][ny] == 0:      #못지나가는 경로일 경우 무시
                continue
            if graph[nx][ny] == 1:          #처음 방문하는 경우에만 거리 기록 (1씩 더해줌)
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))
    return graph[n-1][m-1]          #도착지점까지의 최단 거리 반환

print(bfs(0,0))
