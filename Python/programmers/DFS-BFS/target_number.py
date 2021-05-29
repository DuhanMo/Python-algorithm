# 문제 설명
# n개의 음이 아닌 정수가 있습니다.
# 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers,
# 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서
# 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.


# def solution(numbers, target):
#     tree = [0]
#     for number in numbers:
#         sub_tree = []
#         for tree_num in tree:
#             sub_tree.append(tree_num + number)
#             sub_tree.append(tree_num - number)
#         tree = sub_tree
#         answer = tree.count(target)
#     print(tree)
#     return answer


answer = 0


def dfs(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if (idx == N and target == value):
        answer += 1
        print(idx, numbers, target, value, '결과값 맞아서 함수리턴')
        return
    if (idx == N):
        print(idx, numbers, target, value, '타겟값과 안맞아서 함수 리턴')
        return

    dfs(idx + 1, numbers, target, value + numbers[idx])
    dfs(idx + 1, numbers, target, value - numbers[idx])


def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    print(answer)
    return answer

solution([1,2,3,4,5] , 5)
