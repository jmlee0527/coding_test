#백준 3085번 - 사탕 게임
"""
각 인접하는 행,열에 대해서 바꿔주는 동작, 행,열에 따라 연속된 사탕의 개수를 모두 확인하도록 해야한다.
확인하는 과정이 반복적이고 복잡하여 하나의 함수로 만들어 확인한다.
인접하는 것이 다른 경우 바꾸는 작업을 반복할 때마다 연속된 사탕의 최대 개수를 확인하여 최대값을 구한다.
"""
import sys

n = int(sys.stdin.readline())
candy = []      #2차원 배열 형태로 사탕 종류 저장

def count(candy):       #연속된 최대 사탕 개수를 찾아주는 함수
    max_total = 1
    for i in range(n): 
        total = 1
        for j in range(1,n):         #같은 열에 대해 탐색    
            if candy[i][j] == candy[i][j-1]:
                total +=1
            else:
                total = 1
            max_total = max(max_total,total)
        total = 1
        for j in range(1,n):        #같은 행에 대해 탐색
            if candy[j][i] == candy[j-1][i]:
                total +=1
            else:
                total = 1
            max_total = max(max_total,total)
    return max_total
        

for _ in range(n):
    tmp = list(sys.stdin.readline())
    candy.append(tmp)

result = 0
#인접한 것을 바꾸는 경우 최대 사탕 개수(가로)
for i in range(n):
    for j in range(n):
        if j +1 < n:
                candy[i][j],candy[i][j+1] = candy[i][j+1],candy[i][j]
                #같은 열에서 바꾼 경우 최대값 탐색 - 바꾼 경우 하나씩에 대해서 확인
                result = max(result,count(candy))
                candy[i][j],candy[i][j+1] = candy[i][j+1],candy[i][j]      #다시 원래 배열로 돌려놓기
        if i+ 1< n:
                candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
                #같은 열에서 바꾼 경우 최대값 탐색
                result = max(result,count(candy))
                candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(result)
