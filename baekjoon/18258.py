#백준 18258번 - 큐2
"""
리스트로 구현하는 경우 시간초과 문제가 발생 -> deque 사용
리스트에서 pop() 하는 경우 index를 앞으로 이동하는 만큼 O(n) 시간이 걸림
"""
import sys
from collections import deque
queue = deque()

n = int(sys.stdin.readline())

for i in range(n):
    info = list(sys.stdin.readline().split())

    if info[0] == "push":
        queue.append(info[1])
    elif info[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif info[0] == "size":
        print(len(queue))
    elif info[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif info[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif info[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])    