import sys
input = sys.stdin.readline

n,m = map(int,input().split())

parent = [0]*(n+1)
#parent를 각자 노드로 초기화
for i in range(1,n+1):
    parent[i] = i

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

for _ in range(m):
    num,a,b = map(int,input().split())
    if num == 0:
        union_parent(parent,a,b)        #0인 경우 합치는 과정 진행
    else:
        if find_parent(parent,a) == find_parent(parent,b):
            print("YES")
        else:
            print("NO")