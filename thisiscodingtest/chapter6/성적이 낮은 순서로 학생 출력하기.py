#성적이 낮은 순서로 학생 출력하기
import sys

n = int(sys.stdin.readline())

students = []
for _ in range(n):
    info = list(sys.stdin.readline().split())
    students.append(info)

students = sorted(students,key= lambda info: info[1])

for i in students:
    print(i[0],end = '')
