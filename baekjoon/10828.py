#백준 10828번 - 스택
import sys


n = int(sys.stdin.readline())   #명령어 개수 n

stack =[]   #스택 리스트 초기화

for _ in range(n):
    a = sys.stdin.readline().split()
    inst = a[0]
    if inst == "push":
        num = a[1]
        stack.append(num)       #스택에 값 추가
    elif inst == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())    #스택 가장 뒤의 정수를 pop하고 값을 리턴
    elif inst == "size":
        print(len(stack))       #스택의 사이즈 출력
    elif inst == "empty":   
        if len(stack) == 0:
            print(1)            #비어있는 경우 1출력
        else:
            print(0)            #스택에 값이 있는 경우 0출력
    elif inst == "top":
        if len(stack) == 0:     
            print(-1)
        else:
            print(stack[-1])        #스택의 가장 위 값 출력