#백준 11005번 - 진법 변환2
"""
2745번과 유사하지만 반대로 동작하도록 한다.
b값으로 나눈 나머지값을 통해 b진수의 값을 구할 수 있다.

"""

n,b = map(int,input().split())

value = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ''

while n != 0:
    result += str(value[n%b])
    n = n//b

print(result[::-1])  