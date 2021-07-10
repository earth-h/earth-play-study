# 1920. Build Array from Permutation (시간복잡도: O(n), 공간복잡도: O(1))

## 모듈러(modular) 연산
'''
17 mod 5 = 2
7 mod 11 = 7

a mod n == b mod n => a - b = kn

1920 문제의 경우, 
nums[i] 값이 항상 len(nums)보다 작다.
따라서 nums[a]와 nums[b] 모두 len(nums)보다 작다.

(nums[a] + nums[b] * n) / n = nums[b]
(nums[a] + nums[b] * n) % n = nums[a]

위 내용을 이용해 풀면 O(1) 공간을 가지고 풀 수 있다.
'''
from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        for i in range(0, numsLength):
            nums[i] = nums[i] + (nums[nums[i]] % numsLength) * numsLength
        
        for i in range(0, numsLength):
            nums[i] = int(nums[i] / numsLength)

        return nums

answer = Solution()
#answer.buildArray(list([5,0,1,2,3,4]))
print(answer.buildArray(list([5,0,1,2,3,4])))