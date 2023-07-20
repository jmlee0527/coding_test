#백준 2501번 - 약수 구하기
"""
숫자 n의 약수를 리스트에 저장하고 k번째 값을 출력하도록 한다.
"""
import sys

arr = []

n,k= map(int,sys.stdin.readline().split())

for i in range(1,n+1):
    if n % i == 0:
        arr.append(i)

if len(arr) < k:
    print(0)
else:
    print(arr[k-1])