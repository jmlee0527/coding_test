#음료수 얼려 먹기
"""
그래프 형태로 모델링하여 생각해보기
DFS 알고리즘을 활용하여 0으로 연결되어 있는 부분을 모두 탐색하여 개수를 카운트 하도록 한다.
"""
import sys

graph = []      #인접행렬 정보를 담을 2차원 배열

n,m = map(int,sys.stdin.readline().split())

for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):   
    if x <= -1 or x >=n or y <= -1 or y >= m:  #범위 벗어나는 경우 종류
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1     #0인 경우 방문처리 -> 한번 탐색된 곳을 1로 바뀌어 중복연산하지 않게 된다.
        #상하좌우에 대해 깊이 우선 탐색 진행
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:        #dfs 탐색에 성공한 케이스마다 1씩 더해주므로 총 아이스크림의 수와 동일
            result +=1
print(result)
