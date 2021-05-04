# 큰 수의 법칙

# N, M, K는 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

# 오름차순으로 정렬
data.sort()

'''
특정 인덱스 수가 연속해서 K번을 초과할 수 없고, M개까지 더할 수 있으므로,
제일 큰 수를 K번 더하고, 두 번째 큰 수를 한 번 더하고, 제일 큰 수를 K번 더하고..
반복해서 M번 더하면 답 구할 수 있음
'''

first = data[n - 1]
second = data[n - 2]
result = 0

while True:
    for i in range(k):
        if m == 0:
            break # 가장 가까운 반복문 빠져나감
        result += first
        m -= 1
    if m == 0:
        break # 가장 가까운 반복문 빠져나감
    result += second
    m -= 1

print(result)