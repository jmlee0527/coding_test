'''
DFS 혹은 BFS 알고리즘을 활용하여 풀이가 가능하다.
처음 숫자 단계부터 + 혹은 - 연산 각 경우 모두 연산을 마친 후 target과 같은 수의 개수를 구할 수 있다.

1. 순서대로 +, - 연산을 통해 가능한 모든 수를 저장한다.
2. 매번 부모 노드를 갱신 해주도록 한다.
3. target 과 같은 수의 개수를 찾는다.

'''
def solution(numbers, target):
    answer = 0
    parent = [0]
    for x in numbers:
        tmp = []
        for y in parent:
            tmp.append(y+x)
            tmp.append(y-x)
        parent = tmp
    
    cnt = 0 
    for x in parent:
        if x == target:
            cnt +=1
    answer = cnt
    return answer