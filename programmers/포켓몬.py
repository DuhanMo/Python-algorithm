def solution(nums):
    n = len(nums)/2
    set_nums = set(nums)
    if n < len(set_nums):
        answer = int(n)
    else:
        answer = len(set_nums)
    return answer

# nums = [3,3,3,2,2,4]
nums = [3,1,2,3]
print(solution(nums))