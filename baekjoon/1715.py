#백준 1715번 - 카드 정렬하기
"""
우선순위 큐를 사용하면 자동적으로 작은 것 부터 pop해준다.
최소값을 구하기 위해서는 작은것부터 2개씩 연산을 하면 되므로 우선순위 큐를 사용하여 연산을 진행한다.
"""
import heapq

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))

result = 0


if len(cards)==1:
    print(result)
else:
    for i in range(n-1):
        card1 = heapq.heappop(cards)
        card2 = heapq.heappop(cards)

        result += card1 + card2
        heapq.heappush(cards,card1 + card2)     #다시 cards 리스트에 담아도 작은 것 부터 순차적으로 연산을 진행하므로 상관없음
    
    print(result)




