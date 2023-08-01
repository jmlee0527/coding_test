#백준 10866.py - 덱
"""
deque를 사용하여 조건문을 사용하여 조건에 따라 동작하도록 작성
"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

deque = deque()
for _ in range(n):
    data = list((input().split()))
    if data[0] == "push_front":
        deque.appendleft(data[1])
    elif data[0] == "push_back":
        deque.append(data[1])
    elif data[0] == "pop_front":
        if len(deque) == 0:
            print("-1")
        else:
            print(deque.popleft())
    elif data[0] == "pop_back":
        if len(deque) == 0:
            print("-1")
        else:
            print(deque.pop())
    elif data[0] == "size":
        print(len(deque))
    elif data[0] == "empty":
        if len(deque) != 0:
            print("0")
        else:
            print("1")
    elif data[0] == "front":
        if len(deque) == 0:
            print("-1")
        else:
            print(deque[0])
    elif data[0] == "back":
        if len(deque) == 0:
            print("-1")
        else:
            print(deque[-1])