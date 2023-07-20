#백준 1735번 - 분수 합
"""
분모의 최소 공배수를 구하여 합을 기약분수 형태로 표현할 수 있다.
최대공약수 구하는 방법을 이용하여 최소공배수를 구할 수 있다.
"""
import sys

up = []
down = []

for _ in range(2):
    a,b = map(int,sys.stdin.readline().split())
    up.append(a)
    down.append(b)

m1 = up[0]
m2 = up[1]
n1 = down[0]
n2 = down[1]

#최대공약수 -> 유클리드호제법
def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a

#분자,분모값 구하기
min = gcd(n1,n2)
result2 = (n1//min)*(n2//min)*min
result1 = m1*(result2//n1) + m2*(result2//n2)

#기약분수 형태로 표현하기 위해 최대공약수로 한번 나누어 결과값 출력
result_min = gcd(result1, result2)
print(result1//result_min,result2//result_min)
