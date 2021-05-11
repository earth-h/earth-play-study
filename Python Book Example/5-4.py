# 음료수 얼려 먹기
'''
DFS 이용하여 문제 풀이
1. 특정한 지점의 주변 상/하/좌/우를 살펴본 뒤 주변 지점 중 값이 0이면서 아직 방문하지 않은 지점이 있다면 해당 지점 방문
2. 방문한 지점에서 다시 상/하/좌/우를 살펴보면서 방문 진행하여 연결된 모든 지점 방문
3. 1-2번을 모든 노드에 대해 반복하여, 새로운 1-2번 과정 실행 시마다 카운트를 더한다.
'''

# 입력 받기(n: 세로, m: 가로 1<= n,m <= 1000)
# box 내의 0은 구멍이 뚫린 부분, 1은 그렇지 않은 부분
n, m = map(int, input().split())
boxes = list()
for i in range(n):
    box = list(map(int, input()))
    boxes.append(box)

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 아이스크림 개수
boxCnt = 0

# 방문 여부 확인 변수(2차원 리스트)
visited = [[False] *  m for _ in range(n)]

# DFS 알고리즘 적용
def dfs(graph, visited, x, y):
    visited[x][y] = True
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
            if boxes[new_x][new_y] == 0 and visited[new_x][new_y] == False:
                dfs(graph, visited, new_x, new_y)

for i in range(n):
    for j in range(m):
        if visited[i][j] == False and boxes[i][j] == 0: # 방문하지 않은 위치이고, 구멍이 뚫린 부분인 경우
            boxCnt += 1
            dfs(boxes, visited, i, j)


print(boxCnt)