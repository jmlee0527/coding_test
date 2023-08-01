#백준 1966번 - 프린터 큐
"""
deque를 사용하여 풀이
q가 빌때까지 popleft,append 과정을 반복하여 순서를 알아낸다.
이때 순서를 알기 위한 cnt 값과 본인의 순번을 확인하기 위한 m 값을 매번 갱신해주도록 한다.
"""
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    p= deque(list(map(int,input().split())))
    cnt = 0
    while p:
        p_max = max(p)
        front = p.popleft()
        m -= 1          #한번 pop 할때마다 본인의 차례가 줄어든다.
        if front == p_max:      #가장 우선순위가 커서 출력되는 경우
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            p.append(front)
            if m < 0:
                m = (len(p)-1)      #우선순위가 작아 맨 뒤로 밀려나는 경우 순서를 갱신

