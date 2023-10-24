'''
DFS 알고리즘을 활용하여 연결되어있는 네트워크를 체크한다.
연결이 안되어있는 경우 다시 체크하며 이때마다 카운트를 올려준다.

1. DFS함수를 구현 -> 방문하지 않고 연결되어있는 경우 모두 방문처리하도록
2. 모든 노드에 대해 DFS를 수행하며 방문이 안되어있는 경우에 카운트를 하고 DFS 수행

'''

def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    def dfs(k):
        visited[k] = 1
        for x in range(n):
            if not visited[x] and computers[k][x] ==1:
                dfs(x)
    
    for x in range(n):
        if not visited[x]:
            dfs(x)
            answer += 1

    return answer