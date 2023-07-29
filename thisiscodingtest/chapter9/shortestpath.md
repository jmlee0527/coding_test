# 최단 경로 알고리즘


## 최단 경로 알고리즘
1. 다익스트라 최단 경로 알고리즘
2. 플로이드 워셜
3. 벨만 포드 알고리즘

### 다익스트라 최단 경로 알고리즘
그래프에서 여러 개의 노드가 있을 때, 특정 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
단, 음의 간선이 없을 때 정상적으로 동작한다.
매번 비용이 가장 적은 노드르 선택하여 그리디 알고리즘으로 분류되기도 한다.

출발 노드 설정 -> 최단 거리 테이블 초기화 -> 방문하지 않은 노드중 최단 거리 노드 선택 -> 최단 거리 테이블 갱신하며 반복

### 간단한 다익스트라 알고리즘
매 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 1차원 리스트를 순차탐색한다.
O(V^2)의 시간 복잡도를 갖는다. (V-> 노드의 개수)

#### <간단한 다익스트라 알고리즘 소스코드>

    impmort sys
    input = sys.stdin.readline
    INF = int(1e9)

    n,m = map(int,input().split())
    start = int(input())
    graph = [[] for i in range(n+1)]
    visited = [False]* (n+1)
    distance = [INF] * (n+1)

    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))

    def get_smallest_node():
        min_value = INF
        index = 0
        for i in range(1,n+1):
            if distance[i] < min_value and not visitded[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start):
        distance[start] = 0
        visitded[start] = True
        for j in graph[start]:
            distance[j[0]] = j[1]
        for i in range(n-1):
            now = get_smallest_node()
            visited[now] = True
            for j in graph[now]:
                cost = distance[now]+j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost
    dijkstra(start)

    for i in range(1,n+1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])

### 개선된 다익스트라 알고리즘
개선된 다익스트라 알고리즘을 사용하는 경우 시간복잡도 O(ElogV)를 갖는다. (V->노드 수 , E-> 간선의 개수)
개선된 다익스트라 알고리즘에서는 힙 자료구조를 사용하여 특정 노드까지의 최단 거리에 대한 정보를 담아서 빠르게 탐색이 가능하다.

#### <개선된 다익스트라 알고리즘 소스코드>

    import heapq
    import sys
    input = sys.stdin.readline
    INF = int(1e9)

    #노드,간선의 개수 입력
    n,m = map(int,input().split())
    #시작 노드 번호 입력
    start = int(input())
    #노드간의 연결 정보
    graph = [[] for i in range(n+1)]
    #최단 거리 테이블 초기화
    distance = [INF]*(n+1)

    #간선의 정보 입력 받기
    for _ in range(m):
        a,b,c = map(int, input().split())
        #a 노드에서 b로 가는 비용이 c
        graph[a].append((b,c))

    def dijkstra(start):
        q = []
        #시작 노드로 가기 위한 최단 경로는 0, 큐에 삽입
        heapq.heappus(q,(0,start))
        distance[start] = 0
        while q:
            #가장 최단 거리가 짧은 노드 정보 꺼내기
            dist,now = heapq.heappop(q)
            #이미 처리된 노드인 경우 무시
            if distance[now] <dist:
                continue
            #현재노드의 인접 노드 확인 
            for i in graph[now]:
                cost = dist +i[1]
                #현재 노드를 거쳐 다른 노드 이동 거리가 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heqppush(q,(cost,i[0]))
    dijkstra(start)

    #모든 노드로 가는 최단 거리 출력
    for i in range(1,n+1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])
        
### 플로이드 워셜 알고리즘
플로이드 워셜 알고리즘은 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우에 사용하는 알고리즈이다.


바로 이동하는 거리와 특정한 노드를 거쳐서 이동하는 거리를 비교하여 최소값으로 갱신하는 것이다.


3중 반복문을 사용하여 O(N^3)의 시간복잡도를 갖는다.


#### 플로이드 워셜 알고리즘 소스코드

    INF = int(1e9)

    #노드의 개수 및 간선 개수 입력
    n = int(input())
    m = int(input())

    #2차원 리스트를 만들고 모든 값을 무한으로 초기화
    graph = [[INF]*(n+1) for _ in range(n+1)]

    #자기 자신에서 자기 자신으로 가는 비용은 0
    for a in range(1,n+1):
        for b in range(1,n+1):
            if a == b:
                graph[a][b] = 0

    #각 간선에 대한 정보를 입력받아 초기화
    for _ in range(m):
        #A에서 B로가는 비용 C
        a,b,c = map(int,input().split())
        graph[a][b] = c

    #플로이드 워셜 알고리즘
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

    #결과 출력
    for a in range(1,n+1):
        for b in range(1, n+1):
            if graph[a][b] = INF:
                print("INFINITY", end = " ")
            else:
                print("graph[a][b], end = " ")
        print()