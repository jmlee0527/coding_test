#공 넣기

n,m = map(int,input().split()) # n개의 바구니에 m번 공을 넣음
basket = [0]*n      #비어있는 경우 0으로 초기화

for _ in range(m):
    i,j,k = map(int,input().split())
    for a in range(i-1,j):  
        basket[a] = k

print(*basket)      #리스트 요소를 출력