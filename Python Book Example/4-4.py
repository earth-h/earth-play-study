# 게임 개발

'''
# 왼쪽 회전 하는 부분을 아래와 같이 함수화 가능
def turn_left():
    # global 키워드: 함수 안에서 함수 밖의 변수 데이터 변경
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
'''
# 왼쪽에서 오른쪽: 서쪽에서 동쪽(y+)
# 위에서 아래: 북쪽에서 남쪽(x+)

# direction: 0(북), 1(동), 2(남), 3(서)
n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 기존 방향의 왼쪽으로 가는 경우(북/동/남/서에서 왼쪽방향이므로 순서대로, 서/북/동/남 방향임)
change_direction = [(0, -1), (-1 ,0), (0, 1), (1, 0)]
# 현 방향에서 뒤로 가는 것(북/동/남/서)
back_direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

maps = []
result = 1

for i in range(n):
    maps.append(list(map(int, input().split())))

while True:
    # 상하좌우가 이미 가본 칸이거나, 바다면 뒤쪽 방향으로 갈 것
    check = 0
    for i in range(4):
        nx = x + change_direction[i][0]
        ny = y + change_direction[i][1]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if maps[nx][ny] == 0: # 상하좌우 중에 어딘가 갈 수 있는 육지 존재
                check = 1
                break
    if check == 0: # 상하좌우가 이미 가본 칸이거나, 바다이므로 뒤로 한 칸 갈 것(3)
        nx = x + back_direction[direction][0]
        ny = y + back_direction[direction][1]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if maps[nx][ny] == 1:
                break # 끝내기
            else:
                x = nx
                y = ny
                maps[x][y] = 1 # 움직였으므로 해당 칸도 가본 칸으로 만듬
                result += 1
        else:
            break
    # 상하좌우 중에 어딘가는 갈 수 있는 육지임
    nx = x + change_direction[direction][0]
    ny = y + change_direction[direction][1]
    # 먼저 왼쪽으로 방향 바꾸기
    if direction == 0:
        direction = 3
    else:
        direction -= 1
    if nx < 0 or nx >= n or ny < 0 or ny >= m: # (nx, ny)가 존재하지 않는 칸이면 방향만 바꿈
        continue
    if maps[nx][ny] == 0: # (nx, ny)가 존재하는 칸이고 육지
        x = nx
        y = ny
        maps[x][y] = 1 # 가본 칸으로 만듬
        result += 1

print(result)        
#print(n, m, x, y, direction, maps)
