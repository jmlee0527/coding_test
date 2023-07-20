#공 바꾸기

n,m = map(int,input().split())

basket = [0]*n
for i in range(n):
    basket[i] = i+1     #n개의 바구니를 초기화

for _ in range(m):      #m번만큼 입력받은 두 수의 공을 변경
    a,b = map(int,input().split())
    tmp = basket[a-1]
    basket[a-1] = basket[b-1]   #리스트 인덱스는 0부터 시작하므로 인덱스값 조정
    basket[b-1] = tmp

print(*basket)