#백준 1789번 - 수들의 합
"""
그리디 알고리즘

서로 다른 N개의 자연수가 되려면 1부터 n까지의 숫자로 구성하면 N값이 최대가 된다.
1부터 N까지의 숫자의 합이 s가 되는 n을 찾는다.
"""

s = int(input())

n = 1
sum = 0
while 1:
    sum += n
    if sum > s:
        break
    n += 1

print(n-1)