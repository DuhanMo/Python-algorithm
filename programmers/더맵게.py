import heapq

def solution(scoville, K):
    answer = 0
    # heapq.heapify(scoville)
    print(scoville)
    while scoville[0] < K:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        tmp = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville,tmp)
        print('첫번째작은수, 두번째작은수 빼고 tmp 더하고 ',scoville)
        answer += 1

    return answer


scoville = [  3, 9, 10, 12,2,1]
K = 7
print(solution(scoville, K))
