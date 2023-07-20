#백준 11053번 - 가장 긴 증가하는 부분 수열
"""
동적프로그래밍 방식으로 점화식을 생각하여 풀이
"""
import sys

n = int(sys.stdin.readline())
dp = [1]*n          #수열의 개수를 카운트하기 위한 배열 선언
arr = list(map(int,sys.stdin.readline().split()))

for i in range(n):          
    for j in range(i):      #배열의 앞에서부터 각 경우에 대해 증가하는 수열의 경우 확인
        if arr[i] > arr[j]:     #증가 순열인지 확인
            dp[i] = max(dp[i],dp[j]+1)      #증가 순열인 경우 이전 카운트 최대값에 1을 더해주는 방식

print(max(dp))