#백준 9506번 - 약수들의 합
"""
어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다
본인 숫자를 제외한 약수들을 리스트에 저장하고 합이 숫자 n과 같은지 판별하도록 한다.
"""
import sys

while 1:
    n = int(sys.stdin.readline())
    if n == -1:             #-1이 입력되면 종료
        break
    else:
        arr = []
        for i in range(1,n):
            if n%i == 0:
                arr.append(i)

        if sum(arr) == n:
            print("%s = " %str(n), end ="")
            for i in range(len(arr)-1):
                print(str(arr[i]) + " + ", end ="")
            print(str(arr[-1]))

        else:
            print("%d is NOT perfect." %n)
