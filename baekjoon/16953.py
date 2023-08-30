#백준 16953번 - A->B
"""
그리디 알고리즘

연산속도를 빨리 해주는 것은 1을 마지막에 붙여주는 것이다.
따라서 거꾸로 연산을 수행하며 1이 있는 경우 제거해주고 짝수인 경우 2를 나눠주도록 한다.

"""
a,b = map(int,input().split())

result = 1
while(b!=a):
    result += 1
    tmp = b

    if b%10 == 1:
        b//=10
    elif b%2 == 0:
        b//=2
    
    if tmp == b:
        print(-1)
        break
else:
    print(result)