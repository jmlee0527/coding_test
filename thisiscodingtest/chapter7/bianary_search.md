# 이진탐색 (Binary Search)


## 순차 탐색
리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 순차적으로 확인하는 방법

#### <순차 탐색 소스코드>

    def sequential_search(n,target,array):
        for i in range(n):
            if array[i] == target:
                return i+1

## 이진 탐색
이진 탐색은 배열의 데이터가 정렬되어 있을 때만 사용할 수 있다.


시작점,끝점,중간점 3개의 변수를 사용하여 찾는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교하여 원하는 값을 찾는 알고리즘이다.


이진 탐색의 경우 한 번 확인 시 데이터가 절반씩 줄어들어 효율적으로 O(logN)의 시간복잡도를 갖는다.

#### <이진 탐색 소스코드 - 재귀 함수>

    def binary_search(array,target,start,end):
        if start > end:
            return None
        mid = (start + end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_search(array,target,start,mid-1)
        else:
            return binary_search(array,target,mid+1,end)

#### <이진 탐색 소스코드 - 반복문>

    def binary_search(array,target,start,end):
        while start <= end:
            mid = (start+end) //2
            if array[mid] == target:
                return mid
            elif array[mid] > target:
                end = mid -1
            else:
                start = mid +1
        return None 
