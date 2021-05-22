import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    # 전처리
    remain = [100 - x for x in progresses]
    for i in range(len(remain)):
        remain[i] = math.ceil(remain[i] / speeds[i])
    remain = deque(remain)

    max_num = remain.popleft()
    answer.append(1)
    while remain:
        if remain[0] > max_num:
            answer.append(1)
            max_num = remain.popleft()
        else:
            answer[-1] += 1
            remain.popleft()

    return answer


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))
