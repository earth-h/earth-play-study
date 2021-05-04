# 숫자 카드 게임

# 행의 개수 N과 열의 개수 M을 공백을 기준으로 하여 입력 받기
n, m = map(int, input().split())

min_value = 0 # 1 이상의 값이 행렬의 값으로 나오므로 그보다 작은 0을 min_value로 잡음

for i in range(n):
    data = list(map(int, input().split()))
    data.sort()
    '''
    # 아래 코드 대신 max 함수 사용 가능
    if min_value < data[0]:
        min_value = data[0]
    '''
    # data[0]을 잡기 위해 data.sort()를 하는 대신, min(data)를 사용할 수 있음
    min_value = max(min_value, data[0])

print(min_value)