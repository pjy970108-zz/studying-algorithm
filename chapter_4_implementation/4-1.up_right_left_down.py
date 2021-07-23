n = int(input())
x, y = 1, 1
move = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ["L", "R", "U", "D"]

# 이동 계획 확인
for k in move:
    # 이동 후 좌표 구하기
    for i in range(len(move_type)):
        if k == move_type[i]:
            nx = x+dx[i]
            ny = y+dy[i]
        # 예외
    if nx < 1 or ny <1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)

