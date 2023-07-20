#백준 9095번 - 1, 2, 3 더하기
"""
완전탐색으로 해결
3,2,1 에 각 몇 번을 할당하여 n을 만들 수 있는지 해당 케이스 확인
해당 케이스 별로 순열을 고려하여 횟수 연산

"""
import sys
t = int(sys.stdin.readline())

def factorial(n):       #팩토리얼 연산을 위한 함수 생성
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

for _ in range(t):
    n = int(sys.stdin.readline())
    count = 0           #1,2,3 합으로 나타낼수있는 방법 수
    for i in range((n//3)+1):
        for j in range((n//2)+1):
            for k in range(n+1):
                if (3*i) + (2*j) + (1*k) == n:      #순열을 고려해줘야 한다. 1+3 과 3+1 은 다른 경우이므로!
                    count += factorial(i+j+k) // (factorial(i)*factorial(j)*factorial(k))
    print(count)

