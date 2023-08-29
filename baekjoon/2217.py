#백준 2217번 - 로프
"""
그리디 알고리즘

무게를 입력 받아 정렬한 다음 가능한 경우를 모두 배열에 넣고 최대값을 구한다.
"""

n = int(input())
ropes = []
for i in range(n):
    rope = int(input())
    ropes.append(rope)

ropes.sort()

weight = []
for i in range(n):
    weight.append(ropes[i] * (n-i))

result = max(weight)
print(result)


