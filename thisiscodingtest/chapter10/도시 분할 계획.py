#크루스칼 알고리즘으로 문제를 해결할 수 있다.

import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]= a
    else:
        parent[a] =b

n,m = map(int,input().split())

edges = []
result= 0
last =0         #최소 신장 트리 간선 중 비용이 가장 큰 간선 -> 마을을 두개로 분할
parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort()

for edge in edges:
    c,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += c
        last = c                #정렬된 순서로 하기에 마지막 cost가 최대비용이 된다.
print(result-last)