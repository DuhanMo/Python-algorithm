def solution(board, moves):
    result = []
    answer = 0
    # 인형 뽑기 게임 이동
    for move in moves:
        # 실제 열의 값(인덱스의 시작이 0)은 move - 1
        column = move - 1
        # 행의크기(세로크기) 만큼 반복문
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

# print(solution(board, moves))

for row in range(len(board)):
    for col in range(len(board[row])):
        print(board[row][col], end=' ')
    print()
