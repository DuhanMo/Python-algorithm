n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))


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


n_list.sort()

for m_content in m_list:

    if binary_search(m_content, n_list) is None:
        print(0)
    else:
        print(1)

