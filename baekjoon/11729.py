#백준 11729번 - 하노이 탑 이동 순서
"""
재귀적인 특징을 활용하는 것이 중요!
"""
import sys

def hanoi(n,start,finish):          #재귀함수를 사용하여 n-1개를 두번째판에 모두 옮긴 후 맨 밑을 3번째 판으로 옮긴 다음 다시 2번째판에서 3번째 판으로 이동
    if n == 1:
        print(start,finish)
        return
    else:
        hanoi(n-1,start,6-start-finish)     #n-1개를 2번째판으로 모두 옮김
        print(start,finish)                 #맨 밑 원판을 3번째 판으로 옮김
        hanoi(n-1,6-start-finish,finish)    #2번째 판의 n-1개를 같은 방식으로 3번째 판으로 옮김

n = int(sys.stdin.readline())
print(2**n-1)
hanoi(n,1,3)
