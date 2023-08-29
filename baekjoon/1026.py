#백준 1026번 - 보물
"""
그리디 알고리즘

S의 값이 최소값이 되기 위해서는 A의 최소값 * B의 최대값을 곱하도록 정렬해야한다.
B는 재정렬하면 안되지만 A는 자유롭게 재정렬이 가능하므로 각각 오름차순, 내림차순으로 정리하여 곱한 결과가 결국 최소값이 된다.

"""
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

result = 0
for i in range(n):
    result += a[i]*b[i]

print(result)