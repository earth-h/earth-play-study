# 상하좌우
'''
아래 방식 외에도 주석과 같은 방식으로 처리 가능
n = int(input())
moves = input().split()
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for move in moves:
    for i in len(move_type):
        if move == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            break
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)
'''


# N X N 크기
n = int(input())
# 움직임
# move = input().split()만 해도 충분
move = list(input().split())

# 동작
x = [0, 0, -1, 1]
y = [-1, 1, 0, 0]

point_x = 1
point_y = 1

for i in range(len(move)):
    if(move[i] == 'L'):
        if(1 <= point_y + y[0] <= n):
            point_y += y[0]
    elif(move[i] == 'R'):
        if(1 <= point_y + y[1] <= n):
            point_y += y[1]
    elif(move[i] == 'U'):
        if(1 <= point_x + x[2] <= n):
            point_x += x[2]
    elif(move[i] == 'D'):
        if(1 <= point_x + x[3] <= n):
            point_x += x[3]

print(point_x, point_y)