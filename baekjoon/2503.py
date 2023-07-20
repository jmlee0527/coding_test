#백조누 2503번 - 숫자 야구
"""
모든 경우에 대해 탐색하여 확인하는 완전탐색 유형이다.
1~9의 서로 다른 숫자 순열의 경우를 모두 구한다.
입력받은 스트라이크,볼 개수로 가능한 순열의 개수만 남긴다.
숫자야구에서는 (1,2,3)과 (3,2,1)은 다르기 때문에 순열을 사용하도록 한다.
입력받은 케이스에 해당하는 순열만 남겨두고 해당하지 않으면 지우는 과정을 반복한다.
입력케이스에 해당하는 가능한 순열만 남게된다.
"""
import sys
from itertools import permutations

n = int(sys.stdin.readline())
num = [1,2,3,4,5,6,7,8,9]

perm = list(permutations(num,3))            #순열 생성

for _ in range(n):
    number,strike,ball = map(int,sys.stdin.readline().split())
    number = list(str(number))      #숫자를 리스트로 변환하기 위함 -> number : [1,2,3] 형식
    remove = 0                      #순열을 확인하는 과정에서 삭제하므로 index 범위를 위한 remove 변수 선언
    for i in range(len(perm)):
        strike_cnt = 0              
        ball_cnt = 0
        i -= remove                 #반복문 중 remove한 개수만큼 perm 순열 개수가 줄어들기 때문
        for j in range(3):
            number[j] = int(number[j])      #문자열로 저장되어있으므로 정수형으로 변환
            if number[j] in perm[i]:        #해당 순열에 각 숫자가 포함된 경우 -> strike or ball
                if j == perm[i].index(number[j]):       #인덱스 값이 같은 경우 : strike
                    strike_cnt +=1
                else:
                    ball_cnt +=1
        if strike != strike_cnt or ball != ball_cnt:    #입력받은 케이스의 strike,ball 개수와 비교했을때 결과가 모두 동일해야함
            perm.remove(perm[i])                        #다른 경우 perm 순열에서 삭제
            remove +=1
print(len(perm))            #perm에는 해당 조건을 만족하는 순열만 남음 -> 즉 정답 가능성이 있는 숫자만 남음