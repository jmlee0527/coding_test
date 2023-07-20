#백준 11866 - 요세푸스 문제 0
"""
deque를 사용하여 k번째 요소를 제외하고는 popleft를 하고 다시 append하여 맨 뒤로 보내는 작업을 반복
k번째 요소만 pop 하여 reulst 리스트에 순차적으로 append
"""
import sys
from collections import deque


queue = deque()
result = []

n,k = map(int,sys.stdin.readline().split())

for i in range(1,n+1):
    queue.append(i)

while len(queue)!= 0:
    for i in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<",end="")
for i in range(len(result)-1):
    print("%d, " %result[i],end="")
print(result[-1],end=">")

