#백준 1874번 - 스택수열
"""
문제를 먼저 이해하는 것이 중요!
1.숫자 n을 입력받아 1부터 n까지 숫자 k를 하나씩 입력받는다.
2.입력 받은 숫자 k가 스택에 없다면 순차적으로 추가한 뒤 pop 한다.
3.n== k인 경우 이후에는 반드시 내림차순으로 입력받아야 한다.
4.결과값을 담는 list를 만들어 no가 아닌 경우에만 로그를 출력, no 인 경우 no 문자열만 출력

"""

import sys

n = int(sys.stdin.readline())

stack = []
result = []     #결과값 출력을 위한 리스트
key = 1         #NO 인 경우 key값으로 바로 확인을 위한 변수
idx = 0         #현재 push 한 숫자를 표현

for _ in range(n):
    k = int(sys.stdin.readline())
    if len(stack)!= 0 and stack[-1] == k:   #스택이 비어있지 않고 top값이 k와 같을 때 바로 pop
        stack.pop()
        result.append("-")
    elif len(stack) == 0 or stack[-1] < k:  #스택에 k값 까지 도달하지 않은 경우 idx부터 k값 까지 push
        for i in range(idx+1,k+1):
            stack.append(i)
            idx = k
            result.append("+")
        stack.pop()
        result.append("-")   
    else:
        key = 0

if key == 0:
    print("NO")
else:
    for i in range(len(result)):
        print(result[i])