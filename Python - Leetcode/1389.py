# 1389. Create Target Array in the Given Order

'''
list의 insert 메소드 사용하여 푸는 방식
> list 슬라이싱을 이용해 풀었었는데, 메모리 효율이 좋지 않은 것 같아, insert 사용
'''

from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(index)):
            target.insert(index[i], nums[i])
        return target

ans = Solution()
print(ans.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))