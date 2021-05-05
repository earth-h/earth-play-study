# 시각
# H 입력 받기
h = int(input())

result = 0

for i in range(h + 1): # 시(0시부터 h시까지 이므로 h+1)
    for j in range(60): # 분(00분부터 59분)
        for k in range(60): # 초(00초부터 59초)
            if '3' in str(i) + str(j) + str(k):
                result += 1

print(result)