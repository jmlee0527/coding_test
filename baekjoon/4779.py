#백준 4779번 - 칸토어 집합
"""
재귀적인 성질을 이용하여 선이 하나만 남도록 한다.
3개씩 계속 나누어 최소단위까지 재귀적으로 동작하도록 한다.
가운데를 빈칸으로 바꾸는 동작이므로 좌,우 둘다 재귀적으로 수정작업이 이루어지도록 한다.
"""
import sys

def cantoring(n,start,now_length):      #n -> 앞으로 탐색할 횟수, start ->시작 인덱스 , now_length -> 마지막 인덱스
    if n== 0:
        return
    else:
        length =(now_length-start+1)//3
        cantoring(n-1,start,start+length-1)             #왼쪽
        for i in range(start+length,start+2*length):    #가운데 수정 작업
            line[i] = " "
        cantoring(n-1,start+2*length,start+3*length-1)  #오른쪽

while 1:
    try:
        n= int(sys.stdin.readline())
        line = ["-"] * (3**n)
        cantoring(n,0,len(line))
        print("".join(line))
    except:
        break
        

