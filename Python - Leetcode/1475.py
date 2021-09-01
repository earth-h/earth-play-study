# 1475. Final Prices With a Special Discount in a Shop

'''
monotonic stack 개념
stack의 원소들을 오름차순, 혹은 내림차순 상태로 유지하는 것입니다.
이 개념과 유사하게 stack 내에 list index값을 넣어 오름차순을 유지하도록 해보겠습니다.

enumerate 사용하기
list의 원소와 idx값을 한 번에 for문에서 호출하기 위해 사용합니다.
'''
from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans, stack = prices[:], []
        for idx, price in enumerate(prices):
            while stack and prices[stack[-1]] > price:
                ans[stack.pop()] -= price
            stack.append(idx)
        return ans

ans = Solution()
print(ans.finalPrices([8, 4, 6, 2, 3]))