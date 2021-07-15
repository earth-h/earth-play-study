# 1365. How many Numbers Are Smaller Than the Current Number

'''
기존에는, 리스트를 오름차순으로 정렬하여,
nums 내의 값보다 작은 값들의 개수를 찾아서 답안으로 제시했다.

하지만, 해당 문제에서는 조건으로 nums[i] 값의 범위를 0 <= nums[i] <= 100으로 두었기 때문에
메모리를 조금 더 써서 101개 int를 가지는 list를 생성하여 손쉽게 구할 수 있다.

참고 url
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/discuss/524865/Clean-Python-3-sorting-and-counting
'''

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num = [0] * 101 # 0 ~ 100 인덱스 보유

        for i in nums:
            num[i] += 1 # nums의 원소에 해당하는 인덱스의 값을 1씩 증가
        
        for i in range(1, 100):
            num[i] += num[i - 1] # num[i]는 (i + 1)보다 작은 값들의 개수

        return [num[i - 1] if i > 0 else 0 for i in nums] # 0보다 작은 값은 없기 때문에 if else로 나누었음

ans = Solution()
print(ans.smallerNumbersThanCurrent([44,39,69,51,43,100,93,87,73,63,14,82,48,48,26,71,0,35,81,76,92,94,93,65,25,59,76,66,52,95,91,39,89,21,57,79,85,67]))
