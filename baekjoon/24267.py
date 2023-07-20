#백준 24267번 - 알고리즘 수업 - 알고리즘의 수행 시간 6
"""
MenOfPassion 알고리즘
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}

해당 알고리즘에서 코드1은 3중 for문 내에서 동작하여 i는 1부터 n-2까지, j는 i+1 부터 n-1까지, k는 j+1 부터 n번 동작한다.
ex)
i = 1일 때 1+2+ ... (n-2)번
i = 2일 때 1+2+ ... (n-3)번
의 규칙을 갖고 수행횟수를 하게 된다.
따라서 수행횟수는 (1*2)+(2*3)+ ...+(n-2)*(n-1) //2가 된다.
시간 복잡도는 O(n^3)을 따른다.
"""
import sys
n = int(sys.stdin.readline())
result = 0
for i in range(1,n-1):
    result += i*(i+1)
print(result//2)
print(3)