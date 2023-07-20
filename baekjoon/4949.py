#백준 4949 - 균형잡힌 세상

"""
처음 시도에서는 소괄호,대괄호에 대한 스택을 따로 두고 시작했으나 복잡하게 되었다.
스택 하나를 두고 최근에 소괄호, 대괄호 중 어떤 것이 들어왔는지를 확인하여 yes,no 판별을 진행하도록 수정하였다.
key 값을 사용하여 no 값을 갖는 경우를 판단해주도록 한다.
"""

while 1:
    sentence = list(input())
    if sentence[0] == ".":          #온점 하나만 입력되면 종료
        break
    else:
        stack = [] #소괄호,대괄호 균형확인을 위한 스택
        key = 1
        for tmp in sentence:
            tmp = list(tmp)

            for i in tmp:
                if i == "(":
                    stack.append(i)
                elif i == ")":
                    if len(stack) != 0 and stack[-1] =="(": #스택이 비어있지 않고 최근 스택에 여는 소괄호가 입력된 경우 통과
                        stack.pop()
                    else:
                        key = 0
                elif i == "[":
                    stack.append(i)
                elif i == "]":
                    if len(stack) != 0 and stack[-1] == "[":
                        stack.pop()
                    else:
                        key =0

        if len(stack) == 0 and key ==1:
            print("yes")
        else:
            print("no")