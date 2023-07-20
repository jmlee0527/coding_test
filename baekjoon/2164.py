#백준 2164 - 카드2

"""
큐 자료구조를 사용하여 맨위의 카드를 버리고 그다음 카드를 밑으로 보내는 과정을 반복한다.
"""

import sys
from collections import deque
queue = deque()

n = int(sys.stdin.readline())

for i in range(1,n+1):       #1부터 N까지 큐에 등록
    queue.append(i)

while 1:
    if len(queue) == 1:
        break
    else:
        queue.popleft()         #맨 위의 카드 버리기
        tmp = queue[0]          #그 다음 카드를 tmp에 저장
        queue.popleft()
        queue.append(tmp)       #그 다음 카드를 밑으로 보내기
    
print(queue[0])
