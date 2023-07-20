#백준 13241번 - 최소공배수
"""
유클리드 호제법을 이용하여 최소공배수를 구한다.
: 두 자연수 a,b가 있을 때 a,b의 최대공약수는 a를  b로 나눈 나머지와 b의 최대공약수와 같다. (a>b) -> 나머지가 0이 될때까지 반복

<유클리드 호제법> - 나눗셈
def gcd(x, y):
    if x < y:
        x, y = y, x
    while y != 0:
        x %= y
        x, y = y, x
    return x
"""
import sys

a,b = map(int,sys.stdin.readline().split())

result = a*b            #최소공배수 : 두 수의 곱 // 두 수의 최대공약수

while 1:                #최종 a 값이 최대공약수
    if a > b:
        a, b = b ,a
    b %= a

    if  b == 0:
        break

print(result //a)