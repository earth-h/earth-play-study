# 미로 탈출(dfs 버전)

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

def dfs(graph, visited, x, y, count):
    visited[x][y] = True
    count += 1

    # 함수 밖 변수를 함수 안에서 변경하기 위해 global 지정
    global min_count

    if x == n - 1 and y == m - 1:
        if min_count == 0 or min_count > count:
            min_count = count
            return

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
            if visited[new_x][new_y] == False and graph[new_x][new_y] == 1:
                dfs(graph, visited, new_x, new_y, count)

dfs(miro, visited, 0, 0, min_count)

print(min_count)