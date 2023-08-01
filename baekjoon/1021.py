#백준 1021번 - 회전하는 큐
"""
각각의 수의 인덱스가 앞쪽인지 뒤쪽인지 파악한다.
전체 큐의 중앙 보다 앞쪽에 있는 경우 2번 연산을 수행하는 것이 연산을 최소화 할 수 있다.
반대로 중앙 뒤쪽에 위치하는 경우 3번 연산을 수행하는 것이 연산을 최소화하는 것이다.
따라서 현재 큐의 길이를 절반으로 나누어 앞쪽, 뒤쪽의 경우에 따라 연산을 수행하여 count를 하면 최소값을 구할 수 있다.
"""
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
data = list(map(int,input().split()))

q = deque()
for i in range(1,n+1):
    q.append(i)

count = 0
for x in data:
    while 1:
        if x == q[0]:
            q.popleft()
            break
        else:
            if q.index(x) < len(q)//2+1:
                q.append(q.popleft())
                count +=1
            else:
                q.appendleft(q.pop())
                count +=1

print(count)