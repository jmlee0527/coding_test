#DFS (재귀적 방식)

def dfs(graph,v,visited):       #graph -> 연결 정보 2차원 배열 , v -> 현재 방문 노드 , visited -> 방문 확인 배열
    visited[v] = True   #현재 노드를 방문 처리
    print(v, end = " ")
    for i in graph[v]:      #현재 노드에 연결된 다른 노드 방문
        if not visited[i]:      #방문하지 않은 노드인 경우 재귀적으로 방문
            dfs(graph,i,visited)