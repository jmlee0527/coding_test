#백준 10610번 - 30
"""
그리디 알고리즘

30 = 2*3*5 이므로 30의 배수가 되기 위해서는 마지막 자릿수에 0이 오고 각 자릿수의 합이 3이어야 한다.(0이 없는 경우는 반드시 -1 반환)
-> 배수판정법
"""
n = input()

if "0" not in n:
    print(-1)

else:
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])

    if sum % 3 != 0:        #각 자릿수의 합이 3이 아니면 3의 배수가 될 수 없음
        print(-1)
    else:
        num = sorted(n, reverse=True)
        answer = "".join(num)
        print(answer)


