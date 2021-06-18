from collections import deque


def solution(priorities, location):
    answer = []
    q = deque([(v, i) for i, v in enumerate(priorities)])
    print(q)
    print(max(q)[0])
    while len(q):
        tmp = q.popleft()
        if q and tmp[0] < max(q)[0]:
            q.append(tmp)
        else:
            answer.append(tmp[1])

    return answer.index(location) + 1



priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))
