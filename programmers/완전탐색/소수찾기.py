'''
제안사항의 범위가 적절한 수준인 경우? -> 완전 탐색 방법 고려해보기

1. 가능한 숫자 조합 생성하기 -> permutation을 사용하여 가능한 숫자 조합 생성
2. 소수 인지 확인하기 -> 제곱근까지 확인하여 나누어떨어지는 것이 있는지 확인

'''

from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    
    per = []
    for i in range(1, len(numbers)+1):    
        per += list(permutations(numbers, i))          #i자리 숫자 생성
    
    new_nums = [int(("").join(p)) for p in per]  
    new_nums = list(set(new_nums))      #중복 제거
    
    for x in new_nums:
        check = 0           #소수인지 아닌지 판별하기 위한 변수
        if x<= 1:
            check = 1
        for i in range(2,int(x**0.5) + 1):        # n의 제곱근 보다 작은 숫자까지만 나눗셈
            if x % i == 0:              #나누어떨어지는 수가 있다면 소수가 아님                  
                check = 1
                break
        if check == 0:
            answer += 1
    return answer