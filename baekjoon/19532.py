#백준 19532번 - 수학은 비대면강의입니다.

"""
문자 식 그래도 연립하여 x,y를 각각 a,b,c,d,e,f 로 표현하여 식을 세우는 방식 시도
-> 식을 사용하는 경우 0인 경우 zero division error를 고려해야한다.
브루트 포스 주제에 맞게 모든 경우를 탐색하는 것으로 수정 
"""
import sys
a,b,c,d,e,f = map(int, sys.stdin.readline().split()) 

for x in range(-999,1000):          #x,y에 대해 모든 범위에서 탐색하면서 방정식을 만족시키는 x,y찾기
    for y in range(-999,1000):
        if a*x+b*y == c and d*x+e*y == f:
            result = [x,y]
            break

print(*result)