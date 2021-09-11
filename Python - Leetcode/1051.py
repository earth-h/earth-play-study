# 1051. Height Checker

'''
Counter를 이용해서 heights에 존재하는 숫자별 개수를 구합니다.
그 후, heights를 앞에서부터 확인하면서 올 값을 체크합니다.
이때, 기존과 다른 값이 올 것으로 예측되면 ans ++을 진행합니다.
'''
from typing import List
from collections import Counter

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = Counter(heights)
        i, ans = 1, 0
        for h in heights:
            while cnt[i] == 0:
                i += 1 # height에 존재하는 i가 나올때까지 올림
            if i != h:
                ans += 1 # 만약 이번 차례의 h가 i와 다르면, 현 위치를 i로 바꿔야 함
            cnt[i] -= 1 # 현 위치는 i여야 하므로 cnt[i]에서 하나를 줄여 그 자리를 픽스합니다.
        return ans

ans = Solution()
print(ans.heightChecker([1,1,4,2,1,3]))