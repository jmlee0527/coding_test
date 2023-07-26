#2579번 - 계단 오르기
"""
동적프로그래밍
dp에 누적되 최대 합을 기록한다.
두 계단이 연속되는 경우, 한 계단만 연속으로 올라오는 경우 중 최대값을 구하면 3계단 이상 연속하지 않으면서 최대 합을 구할 수 있다.

"""
import sys
n = int(sys.stdin.readline())

scores = []*n
for _ in range(n):
    scores.append(int(sys.stdin.readline()))

dp = [0]*(n)

if n <= 2:
    print(sum(scores))

else:
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp[2] = scores[1]+scores[2]
    for i in range(2,n):
        dp[i] = max(dp[i-3]+scores[i-1]+scores[i],dp[i-2]+scores[i])        #두 계단 연속, 한 계단 연속으로 올라가는 경우 두가지 중 최대값
    print(dp[-1])