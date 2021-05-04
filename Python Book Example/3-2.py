# 큰 수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 오름차순 정렬
data.sort()

result = 0

# 가장 큰 수가 더해지는 횟수
firstCnt = m % (k + 1) + int(m / (k + 1)) * k
# 두번째로 큰 수가 더해지는 횟수
secondCnt = int(m / (k + 1))

# 가장 큰 수 더해지는 횟수 * 가장 큰 수 + 두번째로 큰 수 더해지는 횟수 * 두번째로 큰 수
result = firstCnt * data[n - 1] + secondCnt * data[n - 2]

print(result)
