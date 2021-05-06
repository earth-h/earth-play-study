# 재귀함수 공부(팩토리얼)

n = int(input())

def factorial_recursive(n):
    if n <= 1: # n이 1 이하이면 1을 반환
        return 1
    return n * factorial_recursive(n - 1)

print(n,'!을 재귀적으로 구현:', factorial_recursive(n))