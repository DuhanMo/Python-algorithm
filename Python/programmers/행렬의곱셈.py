def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp_list = []
        for j in range(len(arr2[0])):
            tmp = 0
            for x in range(len(arr2)):
                tmp += arr1[i][x]*arr2[x][j]
            tmp_list.append(tmp)
        answer.append(tmp_list)


    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

print(solution(arr1, arr2))