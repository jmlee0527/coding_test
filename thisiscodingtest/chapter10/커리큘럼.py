#선수과목과 관련한 내용은 위상정렬 알고리즘을 사용하여 문제를 해결

import sys
from collections import deque
import copy

input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] =b

n = int(input())

parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i

indegree = [0]* (n+1)
time = [0] * (n+1)
graph = [[] for i in range(n+1)]

for i in range(1,n+1):
    info = list(map(int,input().split()))
    time[i] = info[0]
    for x in info[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)    #수행 결과 담는 리스트 -> 리스트의 경우 대입 연산 수행 시 문제가 발생할 수 있으므로 deepcopy() 사용
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i],result[now]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in range(1,n+1):
        print(result[i])
    
topology_sort()