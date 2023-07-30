#백준 1647번 - 도시 분할 계획
"""
기본적으로 크루스칼 알고리즘을 사용하여 풀이가 가능하다.
하지만 두개의 마을로 분리하면서 최소한의 비용을 사용한다.
따라서 가장 비용이 큰 길을 분리하는 것이 최소한의 비용을 사용하게 되는 것이다.
크루스칼 알고리즘을 사용하면서 마지막에 가장 비용이 큰 길을 사용하지 않도록 그만큼의 비용을 빼면 최소 비용을 구할 수 있다.
"""
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
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())

parent = [0] *(n+1)
for i in range(1,n+1):
    parent[i] = i

edges = []
result = 0
last = 0
for i in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort()

for edge in edges:
    c,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += c
        last = c            #경로 계산에 포함되는 값 중 최대값

print(result - last)