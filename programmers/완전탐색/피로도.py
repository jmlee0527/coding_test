'''
주어진 조건의 범위가 제한적이므로 완전 탐색을 고려해본다.

어떻게 모든 순서의 경우를 진행해서 확인할수 있을까?
-> 순열 조합을 사용하여 모든 순서의 경우를 구한다음 진행하자

1. 해당 2차원 배열의 길이 n을 구한다.
2. 0부터 n까지의 숫자 순서 조합을 permutations를 사용하여 구한다.
3. 각 조합을 2차원 배열의 인덱스 값으로 사용하여 진행하여 최대 값을 구하도록 한다.

'''

from itertools import permutations
def solution(k, dungeons):
    answer = -1

    #실행 순서 순열 조합을 구하는 과정
    n = len(dungeons)
    num = [x for x in range(n)]
    per = list(permutations(num))  

    max_cnt = 0

    for p in per:   #각 순열에 대해 확인
        cnt = 0
        tmp_k = k
        for i in p:     #각 순열에서 인덱스 순서대로 진행 (0,1,2)인 경우 i=0 부터 각 과정 진행
            min_t = dungeons[i][0]
            use_t = dungeons[i][1]
            if tmp_k >= min_t:
                tmp_k = tmp_k-use_t
                cnt +=1
        if cnt > max_cnt:
            max_cnt = cnt
    answer = max_cnt
    return answer