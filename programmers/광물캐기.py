#프로그래머스 - 광물캐기

"""
그리디 알고리즘 개념을 사용하여 칠해야 하는 것들을 앞에서 부터 순차적으로 칠하며 횟수를 카운트
wall 리스트에 1은 칠해져 있는 경우 0의 경우 칠해야하는 경우로 표현
"""
def solution(n, m, section):
    answer = 0
    #벽의 초기 상태 세팅
    wall = [1] *n
    for i in section:
        wall[i-1] = 0
        
    #칠해야 하는 부분을 칠하기
    for i in section:
        if wall[i-1] == 0:
            if i <= n-m+1:          #index range 구분을 해줘야 한다!
                for j in range(i-1,i+m-1):
                    wall[j] = 1
                answer +=1
            else:
                for j in range(i-1,n):
                    wall[j] = 1
                answer +=1
    return answer

