def solution(answers):
    answer = []
    count = [0,0,0]
    pattern = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i in range(3):
        for j in range(len(answers)):
            if pattern[i][j % len(pattern[i])] == answers[j]:
                count[i] += 1

    for i in range(3):
        if count[i] == max(count):
            answer.append(i+1)

    return answer



answers = [5, 5, 5, 5, 5]
print(solution(answers))
