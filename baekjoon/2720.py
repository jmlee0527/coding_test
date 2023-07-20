#백준 2720번 - 세탁소 사장 동혁
"""
그리디 알고리즘의 거스름돈 문제와 비슷한 유형으로 생각하고 풀이가 가능하다.
//, % 연산을 활용해 거스름돈을 분배할 수 있다.
"""
import sys

test = int(sys.stdin.readline())

#거스름돈의 종류 선언 (cent 단위로 통일)
quarter = 25
dime = 10
nickel = 5
penny = 1

for _ in range(test):
    price = int(sys.stdin.readline())
    result = [0]*4      #4가지 단위에 대한 개수 0으로 초기화
    while 1:
        if price >= quarter:
            result[0] =(price // quarter)
            price = price % quarter
        elif price >= dime:
            result[1]=(price // dime)
            price = price % dime
        elif price >= nickel:
            result[2]=(price // nickel)
            price = price % nickel
        else:
            result[3]=(price)
            break               #penny단위 까지 거슬러 준후 while 문 종료!
    print(*result)