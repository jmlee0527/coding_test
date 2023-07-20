#백준 26265번 - 알고리즘 수업 - 알고리즘의 수행 시간 4
"""
MenOfPassion 알고리즘
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}

해당 알고리즘에서도 이중 for문 안쪽에서 코드 1이 실행된다.
이때 i 는 1부터 n-1이므로 n-1번, j는 i 부터 n번 실행되므로 총 실행횟수는 0부터 n-1까지의 합이 된다.
0부터 n-1 까지의 합은 (n-1)*n//2번이 된다.
시간 복잡도는 O((n-1)*n//2) 로 최고차항의 계수는 2가 된다.
"""
import sys
n = int(sys.stdin.readline())
print((n*(n-1))//2)
print(2)
