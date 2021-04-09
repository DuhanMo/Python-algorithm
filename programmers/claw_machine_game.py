def solution(board, moves):
    result = []
    answer = 0
    for move in moves:
        column = move - 1
        for row in range(len(board)):
            if board[row][column] == 0:
                continue
            else:
                result.append(board[row][column])
                board[row][column] = 0
                if len(result) > 1 and result[-1] == result[-2]:
                    result.pop()
                    result.pop()
                    answer += 2
                break

    return answer


board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
]


moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))
