def solution(arr1, arr2):
    for x in arr2:
        if x in arr1:
            print(1)
        else:
            print(0)


arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

solution(arr1, arr2)

