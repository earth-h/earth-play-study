# 미로 탈출(bfs - 정답 버전)
from collections import deque

'''
기존 코드에서는 count를 따로 세었지만,
이번 코드는 어짜피 각 칸이 0과 1로 되어 있고, 1일 때만 지나갈 수 있기 때문에
각 칸의 값을 더하는 형태로 진행
'''

# 입력받기
n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]

# 상하좌우 계산 시 사용
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x,y))

    # 큐가 빌때까지 계속
    while queue:
        xx, yy = queue.popleft()

        # 상하좌우 검색
        for i in range(4):
            new_x = xx + dx[i]
            new_y = yy + dy[i]

            # 미로 범위 넘어서면 이번 반복문 아웃
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m:
                continue
            # 괴물 있는 칸이면 이번 반복문 아웃
            if graph[new_x][new_y] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            '''
            BFS는 시작 지점부터 가까운 노드부터 차례대로 노드를 탐색하기 때문에,
            기존에 이미 방문해서 노드 값을 변경시켰다면, 신규 값이 기존에 변경한 노드값보다 클 것이기 때문에
            graph[new_x][new_y]가 1인 경우만 업데이트
            '''
            if graph[new_x][new_y] == 1:
                graph[new_x][new_y] = graph[xx][yy] + 1
                queue.append((new_x, new_y))

    return graph[n - 1][m - 1]

print(bfs(miro, 0, 0))