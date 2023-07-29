#백준 1463번 - 1로 만들기
"""
기본적으로 1을 빼는 연산은 항상 가능하다. 따라서 dp[i] = dp[i-1]+1을 기본식으로 준다.
2,3으로 나누어지는 경우 1을 빼는 것과 나누는 것중 min값을 찾아서 dp에 저장한다.
전형적인 bottom-up 방식으로 dp[n]에 n에 따른 최소 연산수가 저장된다.
"""
import sys

n = int(sys.stdin.readline())
dp=[0]*1000001

for i in range(2,n+1):
    dp[i] = dp[i-1]+1

    if i%2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)
    if i%3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)

print(dp[n])