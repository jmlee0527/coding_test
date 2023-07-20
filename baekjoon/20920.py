#백준 20920번 - 영단어 암기는 괴로워
"""
정렬의 우선순위 역순으로 정렬과정을 진행하도록 한다.
빈도수에 따른 정렬을 위해 딕셔너리 형을 사용한다.
딕셔너리 예시
('sand', 3)
('apple', 2)
('append', 1)
"""
import sys
n,m = map(int,sys.stdin.readline().split())
note = dict()

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) >= m:          #단어의 길이가 m이상인 것만 대상으로 지정
        if word in note:
            note[word] +=1      #이미 있는 경우 빈도수 추가
        else:
            note[word] = 1

note = sorted(note.items(), key = lambda x:(-x[1],-len(x[0]),x[0])) #-x[1] : 빈도수에 따라, -len(x[0]) : 단어의 길이에 따라, x[0] : 알파벳 순

for i in note:
    print(i[0])         #단어만 출력