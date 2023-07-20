#백준 4134번 - 다음 소수
"""
소수를 구하는 방법 -> 하나씩 탐색하는 것 보다는 n의 제곱근 까지만 탐색하는 방식이 시간을 줄여준다!
"""
import sys
import math

def find(n):        #소수임을 판별하는 함수
    if n == 0 or n == 1:
        return 0
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return 0
    return 1        #소수인 경우 1을 반환
    
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    while 1:            #n부터 시작하여 소수일때까지 n에 1씩 더하며 확인
        result = find(n)       
        if result == 1:
            print(n)
            break
        else :
            n += 1
