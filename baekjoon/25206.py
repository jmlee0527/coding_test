#백준 25206번 - 너의 평점은

"""
매번 학점에 따른 경우를 나누기 복잡하여 등급에 따른 점수를 환산하는 함수를 사용
"""

total_count = 0
total_grade = 0 

def trans_grade(n):
    if n == "A+":
        return 4.5
    elif n == "A0":
        return 4.0
    elif n == "B+":
        return 3.5
    elif n == "B0":
        return 3.0
    elif n == "C+":
        return 2.5
    elif n == "C0":
        return 2.0
    elif n == "D+":
        return 1.5
    elif n == "D0":
        return 1.0
    elif n == "F":
        return 0.0
    
for _ in range(20):
    name, count, grade = input().split()
    if grade != "P":            #P인 과목은 학점 계산에 포함하지 않음
        total_count += float(count)
        total_grade += (float(count) * trans_grade(grade))
    
avg = total_grade/total_count
avg = round(avg,6)
print(avg)
