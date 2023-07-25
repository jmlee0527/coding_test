#9461번 - 파도반 수열
"""
점화식 a(n) = a(n-2) + a(n-3)
"""
import sys

t = int(sys.stdin.readline())

dp = [0]*101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for _ in range(t):
    n = int(sys.stdin.readline())
    for i in range(4,n+1):
        dp[i] = dp[i-2] +dp[i-3]
    print(dp[n])