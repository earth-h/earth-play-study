# 1이 될 때까지
'''
먼저, 어떠한 수 N이 K로 나누어 떨어진다면, 나누고 그게 아니면 1을 빼는 식으로 진행
'''
n, k = map(int, input().split())

count = 0

while n > 1:
    if n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)
