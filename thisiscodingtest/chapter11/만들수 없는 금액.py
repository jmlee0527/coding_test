"""
그리디 알고리즘

동전을 이용하여 최솟값을 만들기 위해서는 + 연산을 수행하여 만들 수 없는 값을 찾아야 한다.
1원 동전이 없는 경우에는 반드시 최솟값은 1이다.
target 변수를 update 하면서 만들 수 있는 최솟값을 구한다.

"""
n = int(input())
num = list(map(int,input().split()))

num.sort()

result = 1

for i in num:
    if result < i:
        break
    result += i

print(result)
