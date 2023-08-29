"""
그리디 알고리즘

+, * 만을 사용한다. 0,1이 아닌 경우에는 * 연산을 수행하는 것이 값을 크게 할 수 있다.

"""
su = input()
result = int(su[0])

for i in range (1,len(su)):
    num = int(su[i])
    if result <=1 or num<=1:
        result += num
    else:
        result *= num

print(result)
