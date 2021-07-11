# 1672. Richest Customer Wealth

'''
# for문, if문 한 줄로 코딩하기

1. for문
- 1차원 list의 각 원소 한 줄로 출력하기
v = list(range(10))
print(v)

> 기존
for i in v:
    print(i)

> 한줄
[i for i in v]

=> 위처럼 한줄로 출력할 경우 [0, 1, 2, 3, 4 ..]와 같이 출력됩니다.
이를 좀 더 예쁘게 출력하기 위해서는 ~.join을 이용할 수 있습니다.

print(" ".join(str(i) for i in v))

- 2차원 list의 각 원소 한 줄로 출력하기

> 기존
for i in v:
    for j in i:
        print(j)

> 한줄
[j for i in v for j in i]

2. if문
- one condition

> 기존
if v < 5:
    print(0)

> 한줄(1)
v = 3
if v < 5: print(0)

> 한줄(2)
v = 3
print(0 if v < 5 else 1)

- more than one condition

> 기존
if v < 5:
    print(0)
elif v < 10:
    print(1)
else:
    print(2)

> 한줄로
v = 3
print(0 if v < 5 else 1 if v < 10 else 2)

3. for문 + if문

- if condition에 해당하는 값만 출력하기

v = list(range(10, 20))

> 기존
for i in v:
    if i == 12:
        print(i)

> 한줄로
[i for i in v if i == 12]

- for문에 해당하는 각각의 원소가 if condition에 해당하는지 체크

> 기존
for i in v:
    if i == 12:
        print(i)
    else:
        print("No")

> 한줄로
[i if i == 12 else "No" for i in v]

'''

from typing import List 

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])

answer = Solution()
print(answer.maximumWealth([[1,2,3], [3,2,1]]))