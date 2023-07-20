#백준 25192번 - 인사성 밝은 곰곰이
"""
ENTER 이후 닉네임이 입력되면 카운트를 하도록 한다.
최초 한번만 카운트하기 때문에 닉네임을 리스트로 받아 set형으로 바꾸어 중복을 제거하여 카운트하도록 한다.

"""
import sys
n= int(sys.stdin.readline())
name = []
cnt = 0
for _ in range(n):
    info = sys.stdin.readline().rstrip()    #rstrip 사용하여 개행문자 제거
    if info =="ENTER":          
        name = set(name)        #중복된 닉네임 제거
        cnt += len(name)
        name = []       #ENTER를 입력받는 경우 name 리스트를 초기화
    else:
        name.append(info)

name = set(name)            #중복된 닉네임 제거
cnt += len(name)
print(cnt)
