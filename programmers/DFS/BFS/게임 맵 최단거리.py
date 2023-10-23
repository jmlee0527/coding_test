'''
최단거리를 구하는 문제로 BFS를 활용

1. 각 방향으로 이동하는 dx, dy 생성
2. visited 로 방문 노드 확인 및 deque로 확인 노드 관리
3. 현재 위치에서 각 방향 이동확인하여 가능한 경우 visited 체크 후 deque에 다음 노드 추가

'''

from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    q.append((0,0))
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and maps[ny][nx] ==1:
                visited[ny][nx] = True
                maps[ny][nx] = maps[y][x] +1
                q.append((ny,nx))
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]