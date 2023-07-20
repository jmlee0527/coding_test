#백준 9012번 - 괄호

# "(" 괄호를 스택에 차례로 넣고 ")"가 입력될 때마다 하나씩 pop하여 괄호 개수를 맞춰 VPS를 판단하도록 한다.

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    array = list(sys.stdin.readline())
    stack = []
    key = 0             #스택이 비어있는 상태에서 ")" 입력하는 경우를 위한 변수 설정
    for i in array:         
        if i == "(":
            stack.append(i)     # "(" 입력되는 경우 스택에 삽입
        elif i == ")":
            if len(stack) == 0:
                key = 1         #스택이 비어있는 경우 ")" 입력되는 경우 key 값 변경
                break
            else:
                stack.pop()     # ")" 입력시 pop
    if len(stack) == 0 and key ==0:     #key값이 0이고 스택이 비어있는 경우 VPS로 판별
        print("YES")
    else:
        print("NO")