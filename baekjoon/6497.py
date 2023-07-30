#백준 6497번 - 전력난
"""
거리만큼 비용이 발생한다. 따라서 크루스칼 알고리즘을 사용하여 풀이가 가능하다.
거리가 짧은 집 사이를 우선으로 연결하는 방식으로 비용을 계산할 수 있다.
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
while 1:
    m,n = map(int,input().split())
    if m == n == 0:
        break
    parent = [i for i in range(m)]

    edges = []
    min_price = 0
    for _ in range(n):
        x,y,z = map(int,input().split())
        edges.append((z,x,y))
    edges.sort()

    for edge in edges:
        cost,a,b, = edge
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
        else:
            min_price += cost           #즉 연결에 포함하지 않는 부분의 비용합이 절감하는 비용과 동일

    print(min_price)