#백준 1149번 - RGB거리
"""
2차원 리스트에 각 인덱스에 해당하는 최솟값을 저장해준다.
현재 R을 칠한다면 이전의 G,B 중 최솟값을 더해주는 방식으로 R,G,B에 대한 경우를 각각 저장해주는 것이다.
결과적으로는 고른 색에 따른 최솟값이 형성 되므로 마지막 배열에서 최솟값을 구해준다.
"""
import sys

n = int(sys.stdin.readline())
dp =[]
for _ in range(n):
    dp.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,n):
    dp[i][0] = dp[i][0]+ min(dp[i-1][1],dp[i-1][2])
    dp[i][1] = dp[i][1]+ min(dp[i-1][0],dp[i-1][2])
    dp[i][2] = dp[i][2]+ min(dp[i-1][0],dp[i-1][1])

print(min(dp[-1]))