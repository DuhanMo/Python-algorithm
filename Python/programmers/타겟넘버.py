answer = 0


def dfs(idx, n_sum, target, numbers):
    global answer
    n = len(numbers)
    if idx == n:
        if n_sum == target:
            answer += 1
        return

    else:
        dfs(idx+1, n_sum + numbers[idx], target, numbers)
        dfs(idx+1, n_sum - numbers[idx], target, numbers)


def solution(numbers, target):
    global answer
    dfs(0, 0, target, numbers)

    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
