#백준 24266번 - 알고리즘 수업 - 알고리즘의 수행 시간 5
"""
MenOfPassion 알고리즘
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            for k <- 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}

해당 알고리즘에서 코드1은 3중 for문 내에 위치하고 각각 n번 수행하므로 총 n**3번 수행하게 된다.
시간 복잡도는 O(n^3)으로 최고차항의 계수는 3이다.
"""
import sys
n = int(sys.stdin.readline())
print(n**3)
print(3)