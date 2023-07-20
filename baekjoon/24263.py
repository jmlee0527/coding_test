#백준 24263번 - 알고리즘 수업 - 알고리즘의 수행 시간 2
"""
알고리즘
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        sum <- sum + A[i]; # 코드1
    return sum;
}

해당 알고리즘에서 for문을 통해 1부터 n까지 수행하게 된다.
따라서 코드1의 수행횟수는 n번이 된다. 시간 복잡도도 O(n)을 따르게 된다.
"""
import sys
n = int(sys.stdin.readline())
print(n)
print(1)