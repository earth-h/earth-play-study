'''
1877. Minimize Maximum Pair Sum in Array

pair의 max값 중 minimum 값을 찾아야 하므로,
max값이 제일 작아야 합니다. 
따라서, List를 정렬해서 제일 큰 값과 제일 작은 값을 pair로 잡는 식으로
pair를 만든 후, 해당 sum 값들 중 제일 큰 값을 return하면 됩니다.

* 처음에는 pairSums이라는 list를 만들어서 nums[i] + nums[len(nums) - i - 1] 결과를 저장했지만,
그렇게 하면 메모리를 더 사용하게 될 것 같아 ans 변수를 만들어 ans 변수가 pair의 sum 값보다 작으면 업데이트 하는 방식으로 진행했습니다.

Runtime: 1140 ms, faster than 93.91% of Python3 online submissions for Minimize Maximum Pair Sum in Array.
Memory Usage: 28.1 MB, less than 48.77% of Python3 online submissions for Minimize Maximum Pair Sum in Array.
'''

from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        ans = 0
        
        for i in range(n // 2):
            if ans < nums[i] + nums[n - i - 1]:
                ans = nums[i] + nums[n - i - 1]

        return ans

solution = Solution()
print(solution.minPairSum([3,5,2,3]))