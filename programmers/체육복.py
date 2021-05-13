def solution(n, lost, reserve):

    # 전처리
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    print('set_lost',set_lost)
    print('set_reserve',set_reserve)

    for i in set_reserve:
        if i + 1 in set_lost:
            set_lost.remove(i+1)
        elif i - 1 in set_lost:
            set_lost.remove(i-1)

    return n - len(set_lost)


n = 4
lost = [3, 1, 2]
reserve = [2, 4, 3]
print(solution(n, lost, reserve))
