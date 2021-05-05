# 왕실의 나이트
'''
아래 방식 외에도 주석과 같은 방식으로 처리 가능
location = input()

x = int(ord(location[0])) - int(ord('a')) + 1
y = int(location[1])

result = 0
steps = [(2,-1), (2,1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        result += 1

print(result)
'''

# 위치는 8 X 8이므로, (1,1) ~ (8,8)로 생각

location = input()

alpa_x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# 나이트가 움직일 수 있는 방향
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

x = 0
y = int(location[1])

result = 0

# 먼저 나이트 x 위치를 잡는다
for i in range(len(alpa_x)):
    if location[0] == alpa_x[i]:
        x = i + 1
        break

# 8가지 방법 중 가능한 움직임 체크
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if(1 > nx or 8 < nx or 1 > ny or 8 < ny):
        continue
    result += 1

print(result)