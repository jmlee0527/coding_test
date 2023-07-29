#백준 10844번 - 쉬운 계단 수
"""
2차원 배열 dp를 사용한다. dp[i][j]에서 i는 자릿수 n을 의미하고 [0]~[9] 배열에 각각 0부터 9로 끝나는 수의 개수를 기록한다.
i번째 자릿수에서 dp[i][0]의 경우 0으로 끝나려면 앞에는 1로 끝나는 dp[i-1][1]개의 경우를 붙일 수 있는 것이다.
0,9의 경우에만 1,8이 붙을 수 있는 것을 고려하여 점화식으로 표현이 가능하다.
"""
import sys
n = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(n+1)]

for i in range(1,10):
    dp[1][i] = 1

for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]

print(sum(dp[n])%1000000000)
