
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        # skill_tree 기준으로 skill과의 중복원소를 순서유지해서 찾아냄
        result = [x for x in skill_tree if x in skill]
        # result와 skill의 순서를 같은크기로 맞춘 후에 같으면 카운트1 증가
        if result == list(skill)[:len(result)]:
            answer += 1

    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))
