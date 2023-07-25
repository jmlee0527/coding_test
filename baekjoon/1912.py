#1912번 - 연속합
"""
dp에 n번째까지의 최대 연속합을 저장한 후 최대값을 출력하도록 한다.
n번째 수와 n번째 이전의 합(dp에 저장)을 비교하여 최대 연속합을 구할 수 있다.
"""
import sys
n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))
dp = [0] * (n)

dp[0] = arr[0]
for i in range(1,n):
    dp[i] = max(arr[i],arr[i]+dp[i-1])          #현재 값과 이전값 + 현재값을 비교하여 dp에 저장한다.

print(max(dp))
