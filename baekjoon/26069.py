#백준 26069번 - 붙임성 좋은 총총이
"""
처음에는 총총이만 춤을 추는 것으로 춤을 추는 사람들을 리스트로 관리
두 사람 중 한 사람이 리스트에 포함되어있다면 다른 사람도 리스트에 더하는 방식으로 진행
"""
import sys
n = int(sys.stdin.readline())

dancer = ["ChongChong"]         #춤을 추는 사람들을 리스트로 관리

for _ in range(n):
    man1, man2 = sys.stdin.readline().split()
    if man1 in dancer:
        dancer.append(man2)
    elif man2 in dancer:
        dancer.append(man1)

dancer = set(dancer)        #중복 인원 제거
print(len(dancer))
