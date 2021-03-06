# 1이 될 때까지
# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 합니다.
# 단 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺍니다
# 2. N을 K로 나눕니다
# 예를 들어 N이17, K가 4라고 가정합시다. 이때 1번의 과정을 한번 수행하면 N은 16이 됩니다.
# 이후에 2번의 과정을 두번 수행하면 N은 1이 됩니다. 결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 됩니다. 이는 N을 1로 만드는 최소 횟숭입니다.
# N과 K가 주어질 때 N이 1이 될 때 까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하세요.

# 아이디어
# 주어진 N에 대하여 최대한 많이 나누기 실행
# N의 값을 줄일 때 2 이상의 수로 나누는 작업이1을 빼는 작업보다 수를 훨씬 많이 줄일 수 있음
# 정당성 분석 : 가능하면 최대한ㅇ 많이 나누는 작업이 최적의 해를 보장할 수 있나??
# N이 아무리 큰수여로 K로 계속 나눈다면 기하급수적으로 빠르게 나눌 수 있음
# n, k = map(int, input().split())
#
# result = 0
#
# while True:
#     target = (n // k) * k
#     result += (n - target)
#     n = target
#     if n < k:
#         break
#     result += 1
#     n //= k
#
# result -= 1
# print(result)



n, k = map(int, input().split())

result = 0
# n 27 k 7
while True:
    target = (n//k) * k  # target = 21 , 0
    result += n - target  # result = 6,7  +3 -> 10
    n = target  # n = 21, n = 0
    if n < k:
        break
    result += 1  # result = 7
    n //= k  # n = 3

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)  # 10-1 (n이 0이되어버렷어,)
print(result)

