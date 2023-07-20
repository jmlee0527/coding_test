#백준 2745번 - 진법 변환
"""
ord()함수를 이용하여 알파벳의 아스키코드 값을 확인 할 수 있다.
"1" -> 49
"9" -> 57
"A"  -> 65

리스트로 입력 받아 reverse를 하여 index를 지수로 활용하여 계산하도록 하였다.
"""
n,b = input().split()

n = list(n)
n.reverse()
b = int(b)

result = 0
for i in range(len(n)):
    if ord(n[i]) < 58 :
        result += int(n[i]) * (b**(i))
    else:
        tmp  = ord(n[i]) - 55
        result += tmp * (b**(i))

print(result)
