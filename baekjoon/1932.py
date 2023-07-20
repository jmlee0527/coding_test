#백준 1932번 - 정수 삼각형
"""
피라미드 삼각형 구조에서 위에서부터 큰 값을 골라서 차례대로 더하여 마지막 줄의 최대값을 구하도록 한다.
"""
import sys

n = int(sys.stdin.readline())

dp = []             #숫자를 차례로 담을 이차원 배열 생성
for i in range(n):
    dp.append(list(map(int,sys.stdin.readline().split())))  #각줄의 수를 리스트 형태로 받아 그대로 2차원배열 형태로 저장

for i in range(1,n):            #i는 2차원 배열에서 row를 의미, 1부터 시작 - 0번째는 첫번째 숫자 그대로 존재
    for j in range(i+1):
        if j == 0:              #각 줄의 첫번째 요소는 윗 줄의 첫번째 요소만 더할 수 있음(앞쪽 끝)
            dp[i][j] += dp[i-1][j]
        elif j == i:            #각 줄의 마지막 요소는 윗 줄의 마지막 요소만 더할 수 있음(뒤쪽 끝)
            dp[i][j] += dp[i-1][j-1] 
        else:                   #그 외의 중간에 있는 경우 윗줄의 양옆의 값 중 최대값을 더함
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])

print(max(dp[n-1]))         #마지막 줄의 최댓값이 구하고자 하는 값