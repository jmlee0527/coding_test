'''
노란색 카펫의 배열 모양에 따라 전체 카펫 모양이 결정된다.

1. 노란색 카펫 형태 경우의 수를 모두 구한다. -> 약수들의 곱
2. 각 해당 경우 갈색 카펫의 개수를 구한다. -> 노란색의 가로 +2 * 노란색의 새로 +2
3. 해당 경우 카펫의 개수가 주어진 값과 동일할때까지 완전 탐색
4. 같은 경우 결과 출력

'''

def solution(brown, yellow):
    answer = []
    x = 0
    y = 0
    for i in range(yellow,0,-1):        #가로가 더 크때문에 큰 값부터 낮춰가며 진행
        x = 0
        y = 0
        if yellow %i == 0:
            x = i
            y = yellow//i
            if 2*x +2*(y+2) == brown:
                answer.append(x+2)
                answer.append(y+2)
                break
            
    return answer