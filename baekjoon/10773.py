#제로
import sys

k = int(sys.stdin.readline())
stack = []      #스택 구조로 관리

for _ in range(k):
    num =int(sys.stdin.readline())
    if num == 0:        #0을 입력받은 경우 스택에서 최근의 숫자를 삭제
        stack.pop()
    else:
        stack.append(num)

result = sum(stack)     #su
print(result)