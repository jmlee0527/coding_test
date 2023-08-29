"""
그리디 알고리즘

문자열이 연속되는 과정에서 바뀌는 횟수를 구한다.
문자열 마지막에 바뀌는 경우를 생각해준다.
0과 1로 바꾸는 각각의 경우를 생각해줘야 한다. 
"""

s = input()

count0 =0
count1 =0

if s[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count0 +=1
        else:
            count1 +=1

result = min(count0,count1)
print(result)