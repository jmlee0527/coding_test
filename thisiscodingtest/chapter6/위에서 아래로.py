# 위에서 아래로

# 1.파이썬 라이브러리 사용
import sys

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    num= int(sys.stdin.readline())
    nums.append(num)

nums.sort(reverse=True)

print(*nums)

# 2. 선택 정렬 풀이
import sys

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    num= int(sys.stdin.readline())
    nums.append(num)

for i in range(len(nums)):
    max = i
    for j in range(len(nums),i+1,-1):
        if nums[max] < nums[j]:
            max = j
    nums[max], nums[j] = nums[j],nums[max]

print(*nums)

