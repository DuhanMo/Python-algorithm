# DFS 소스코드 예제

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    # 보통 노드가 1번부터 시작하기에 0번을 비워둠
    [],
    [2, 3, 8],  # 1번 노드에 인접한 인덱스 표현
    [1, 7],  # 2번노드에 인접한 인덱스 표현
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
# False를 통해서 모든 노드를 방문하지 않은것처럼 처리 , 0번인덱스 사용하지 않지만 False처리 하기위해 9까지 곱해줌
visited = [False] * 9

# 정의 된 DFS함수를 호출
dfs(graph, 1, visited)
