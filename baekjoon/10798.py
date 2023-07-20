#백준 10798번 - 세로읽기
"""
문자를 2차원 배열로 입력 받아 출력시 행과 열을 바꾸어 순서대로 출력하도록 구현
각 줄의 글자수가 다른 경우에 대한 고려
"""

arr = []    #문자를 입력받는 2차원 배열 선언
result = []     #결과값 출력을 위한 배열 선언
max = 0
for _ in range(5):
    a = list(input())
    arr.append(a)
    if len(a)>max:
        max = len(a)

for i in range(max):
    for j in range(5):
        if i < len(arr[j]):
            new = arr[j][i]     #행,열을 반대로 하여 세로로 읽음
            result.append(new)     #읽은 문자를 리스트에 순차적으로 저장

print("".join(result))      #리스트 요소를 빈칸없이 join 하여 출력
