#백준 2447번 - 별 찍기 - 10
"""

"""
import sys
n = int(sys.stdin.readline())
star = [['*']*n]*n

def change(n,row,col):
    if n == 3:
        return
    else:
        n = n//3
        change(n,
        for i in range(row+2*n,row+2*n):
            for j in range(col+n,col+2*n):
                star[i][j] = " "





for i in range(n):
    print(*star[i])