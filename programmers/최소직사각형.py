"""
완전탐색

가로,세로 중 큰 값, 작은 값을 각각 따로 모아 각 리스트의 최대값의 곱을 구한다 .
"""
def solution(sizes):
    answer = 0
    x = []
    y = []
    for card in sizes:
        if card[0] > card[1]:
            x.append(card[0])
            y.append(card[1])
        else:
            x.append(card[1])
            y.append(card[0])
    answer = max(x) * max(y)
    return answer