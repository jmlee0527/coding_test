#백준 1922번 - 네트워크 연결
"""
크루스칼 알고리즘을 사용한 풀이
"""
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a <b :
        parent[b] =a
    else:
        parent[a] =b

parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

edges =[]
result = 0      #비용을 저장할 변수
for i in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort()        #비용이 작은 경우부터 찾아가는 것 -> 그리디 개념

for edge in edges:
    c,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):          #같지 않다면 연결되어있지 않은 경우
        union_parent(parent,a,b)            #이제 연결됨을 의미
        result += c
    
print(result)
