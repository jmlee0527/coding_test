"""
문자열을 리스트로 변환하여 순환하며 갯수를 확인합니다.
갯수가 같은 경우 해당 문자열 앞부분을 슬라이싱 하고 다시 해당 지점 부터 진행합니다. 이때 전체 result 값을 +1 합니다.
남은 부분에 대한 문자열 1개를 마지막에 추가합니다.
"""
def solution(s):
    answer = 0
    s = list(s)
    x = s[0]
    cnt1 = 0
    cnt2 = 0
    for i in range(len(s)-1):
        if s[i] == x:
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 == cnt2:
            answer +=1
            cnt1 = 0
            cnt2 = 0
            x = s[i+1]
    return answer+1