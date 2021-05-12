# 미로 탈출(bfs 버전)
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# N X M 칸
n, m = map(int, input().split())

# miro[x][y] == 0이면 괴물 있어서 가면 안 됨
miro = [list(map(int, input())) for _ in range(n)]

# 방문 여부 체크(2차원 리스트)
visited = [[False] * m for _ in range(n)]

# 최소 카운트
min_count = 0

def bfs(graph, visited, x, y, count):
    visited[x][y] = True
    queue = deque()
    queue.append((x,y, count))

    global min_count

    while queue:
        xx, yy, ccount = queue.popleft()
        ccount += 1
        if xx == n - 1 and yy == m - 1:
            if min_count == 0 or min_count > ccount:
                min_count = ccount
                continue
        for i in range(4):
            new_x = xx + dx[i]
            new_y = yy + dy[i]
            if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
                if visited[new_x][new_y] == False and miro[new_x][new_y] == 1:
                    queue.append((new_x, new_y, ccount))
                    visited[new_x][new_y] = True

bfs(miro, visited, 0, 0, min_count)

print(min_count)