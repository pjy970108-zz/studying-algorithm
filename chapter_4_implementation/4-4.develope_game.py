n , m = map(int, input().split())

d = [[0]*m for _ in range(n)] # n*m 빈리스트 생성

x, y, direction = map(int, input().split())

d[x][y] = 1 # 현재 좌표 초기화 

array = []

for i in range(n):
    array.append(list(map(int, input().split()))) # N개의 전체 맵 정보 받아옴

dx = [-1, 0, 1, 0] # 북, 남
dy = [0, 1, 0, -1] # 동, 서

def turn_left():
    global direction # 전역 위치 받아오기
    direction -= 1
    if direction == -1: # 다 회전 했을경우
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전 후 가보지 않은 칸이 있으면 
    if d[nx][ny] == 0 and array[nx][ny]== 0:
        d[nx][ny] = 1 # 육지를 1로 바꿈
        x = nx # X 위치 변경
        y = ny # y 위치 변경
        count += 1
        turn_time = 0
    else:
        turn_time += 1
    # 네방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로갈 수 있으면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)

