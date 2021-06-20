def binary_search(target, data):
    # data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid  # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


# n = int(input())
# n_list = list(map(int, input().split()))
#
# m = int(input())
# m_list = list(map(int, input().split()))

answer = []

n_list = [6, 3, 2, 10, -10]
m_list = [10, 9, -5, 2, 3, 4, 5, -10]

n_list.sort()
for x in m_list:
    if binary_search(x, n_list) is not None:
        print(1, end=" ")
    else:
        print(0, end=" ")

# int형 list join 함수 쓰기
# print(" ".join(map(str, n_list)))
