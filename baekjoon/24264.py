#백준 24264번 - 알고리즘 수업 - 알고리즘의 수행 시간 3
"""
알고리즘
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}

해당 알고리즘에서 코드1 은 2중 for문 안쪽에 위치하여 i, j가 각각 n번씩 반복되며 수행하게 되어 총 n*n번 수행하게 된다.
시간 복잡도는 O(n^2)가 된다.
"""
import sys
n = int(sys.stdin.readline())
print(n**2)
print(2)
