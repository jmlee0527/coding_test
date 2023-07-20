#백준 24313번 - 알고리즘 수업 - 점근적 표기 1
"""
함수 f(n) = a1n + a0, 양의 정수 c, n0가 주어질 경우 O(n) 정의를 만족하는지 알아보자.

판별식을 세워 조건이 성립하는지 확인한다.
a1 <= c 조건을 추가해야한다.

"""
import sys
a1, a0 = map(int,sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

f = a1* n0 + a0

if f <= c*n0 and a1<=c:
    print(1)
else:
    print(0)