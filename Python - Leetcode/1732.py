# 1732. Find the Highest Altitude

'''
itertools의 accumulate 함수 사용
> accumulate 함수를 이용하면, 누적합을 구할 수 있습니다.
해당 누적합은, list로 묶어야 list로 뽑아낼 수 있습니다.
'''

from itertools import accumulate
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max([0] + list(accumulate(gain)))

ans = Solution()
print(ans.largestAltitude([-5, 1, 5, 0, -7]))