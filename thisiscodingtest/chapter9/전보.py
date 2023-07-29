import sys
import heapq
input = sys.stdin.readline

n,m,c = map(int,input().split())
INF = (1e9)
distance = [INF] *(n+1)
graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(m):
    #x에서 y로 이어지는 통로 존재 & 메시지 전달 시간 z
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    #시작 노드로 가는 경로는 0으로 설정
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] <dist:
            continue
        #인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)
count = 0
max_dis = 0

for i in distance:
    if i!= INF:
        count +=1
        max_dis = max(max_dis,i)
print(count-1,max_dis)