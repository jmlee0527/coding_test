#백준 2903 - 중앙 이동 알고리즘
"""
수학적 공식을 활용하여 문제를 해결하였다.
결국 i 번째에는 k*k 의 개수를 갖는다.
i 번째 -> k * k
i+1번째 -> ((k*2)-1)*((k*2)-1)
위의 규칙을 갖고 개수를 갖게 됨을 알 수 있다.
"""
import sys

n = int(sys.stdin.readline())

start = 3
if n == 1:
    result = start * start
else:       
    for _ in range(1,n):
        start = (start*2)-1
    result = start * start

print(result)