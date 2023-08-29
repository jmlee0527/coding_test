#백준 5430번 - AC
"""
"""
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = list(input())
    n = int(input())
    data = deque(list(input().split("",",")))
    data = data[1:-1]
    for i in range(len(p)):
        if p[i] == "R":
            data.reverse()
        elif p[i] == "D":
            if len(data) == 0:
                print("error")
            else:
                data.popleft()
    print(data)