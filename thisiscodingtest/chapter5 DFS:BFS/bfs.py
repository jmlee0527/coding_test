from collections import deque

def bfs(graph,start,visited):   #graph -> 인접 노드 정보 2차원 배열 , start -> 탐색 시작 노드 , visited -> 방문 확인 배열
    queue = deque([start])
    visited[start] = True       #현재 노드 방문 처리
    while queue :   #queue가 빌때까지 -> 탐색할 인접노드가 없을 때까지 반복
        v = queue.popleft()
        print(v,end = " ")
        for i in graph[v]:      #현재 노드와 인접한 노드 중 방문하지 않은 원소를 큐에 추가
            if not visited[i]:
                queue.append(i)
                visited[i] = True

