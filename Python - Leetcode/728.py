# 728. Self Dividing Numbers

'''
for 반복문과 else를 이용해보자.

python의 경우, for 반복문을 else와 함께 사용할 수 있습니다.

for 변수 in 반복가능자:
    수행문1
else:
    수행문2

* 위 상황에서 for문의 마지막 요소까지 모두 반복하면, else를 수행하게 됩니다.

예를 들어, 아래와 같은 코드가 있다면, break으로 인해 for문에서 빠져나가지 않고 모든 반복문을 수행했을 때, else 구문이 실행됩니다.
for 변수 in 반복 가능자:
    if 조건문:
        break
else:
    수행문2

'''
from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            for s in str(i):
                if s == '0' or i % int(s) != 0:
                    break
            else:
                ans.append(i)
        return ans

ans = Solution()
print(ans.selfDividingNumbers(1, 22))