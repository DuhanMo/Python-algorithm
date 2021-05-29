# 구현
# 여행가 A의 이동후 좌표


# 1. 몇칸갈지 입력받기
# 2. 어디로 가는지 이동받기
# 3. 좌표 설정
# 4. 이동기 설정

n = int(input())
plans = input().split()
x, y = 1, 1
# L R U D 에 따른 이동방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
