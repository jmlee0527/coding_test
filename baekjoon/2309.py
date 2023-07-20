#백준 2309번 - 일곱 난쟁이
"""
9개중 7개를 고르는 모든 경우의 수에 대해 더하기 연산을 수행해서 100이 되는지 확인하도록 한다.
combinations를 사용하여 9C7의 조합 경우의 수를 리스트에 저장한다.
리스트의 각 경우에 대해 합이 100이 되는지 확인하도록 한다.
"""
import sys
from itertools import combinations

index = [0,1,2,3,4,5,6,7,8]     #조합에 사용될 가능한 인덱스 숫자
comb = list(combinations(index,7))      #9개중 7개를 고르는 모든 경우의 수

height =[]         
for _ in range(9):          #9 난쟁이의 키를 리스트에 저장
    h = int(sys.stdin.readline())
    height.append(h)

for case in comb:           #각 조합의 경우에 대해 탐색
    total = 0
    case_height = []             #키의 합이 100이 되는지 확인하며 result에 바로 7명의 키를 담는다.
    for i in range(7):
        total += height[case[i]]        #7명의 키의 합을 구한다.
        case_height.append(height[case[i]])  #for문을 돌며 7명 키를 result에 저장
    if total == 100:
        answer = case_height     #키의 합이 100인 경우 result가 구하고자 하는 답
answer.sort()       #오름차순으로 정렬
for i in answer:
    print(i)