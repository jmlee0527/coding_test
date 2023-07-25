#신나는 함수 실행
"""
기존의 재귀함수를 보고 동적 프로그래밍 방식을 떠올릴 수 있다.
재귀 함수의 경우 매 계산마다 새로 계산을 하기 때문에 실행 시간이 오래 걸린다.
하지만 동적 프로그래밍 방식을 사용하면 한번 계산한 함수의 내용을 리스트에 저장해두고 찾아 사용하도록 하여 실행 시간을 줄일 수 있다.
예를 들어 w(10,2,3)을 구하는 과정에서 계산된 값들을 3차원 배열 d[][][] 의 인덱스값을 활용해 값을 저장해 둘 수 있다.
추가적으로 20보다 큰 경우 모두 20,20,20이라는 점에서 3차원 배열의 크기는 21만 있다면 충분함을 알 수 있다.

"""
import sys

def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20,20,20)
    if d[a][b][c] != 0:         #이미 계산되어있는지 확인
        return d[a][b][c]       
    if a<b<c:
        d[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return d[a][b][c]
    d[a][b][c] =  w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return d[a][b][c]

d = [[[0]*(21) for _ in range(21)] for _ in range(21)]

while 1:
    a,b,c = map(int,sys.stdin.readline().split())
    if a == -1 and b == -1 and c== -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
