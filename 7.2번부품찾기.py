n = int(input())
array = list(map(int,input().split()))
m = int(input())

for i in m:
    if m in array:
        print("yes",end=" ")
    else:
        print("no",end=" ")

"""추가 답안
이진 탐색색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

# 입력 처리
n = int(input())
array = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

# 배열 정렬 (이진 탐색을 위해)
array.sort()

# 각 타겟에 대해 이진 탐색 수행
for target in targets:
    if binary_search(array, target, 0, n - 1):
        print("yes", end=" ")
    else:
        print("no", end=" ")
"""
"""추가 답안
계수 정렬
n = int(input())
array = [0] * 1000001
for i in input().split():
    array[i] = 1
m = int(input())
for i in input().split():
    if array[i] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
"""

