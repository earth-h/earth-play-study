# 1313. Decompress Run-Length Encoded List

'''
extend 개념 잡기
> append와 달리 list.extend(iterable)로, 인자로 넘겨준 값의 각 원소를 list의 원소로 각각 넣는다.

예시)
# append
>>> sample = ['earth', 'moon']
>>> test = ['red', 'blue']
>>> sample.append(test)
>>> print(sample)
['earth', 'moon', ['red', 'blue']]

# extend
>>> sample = ['earth', 'moon']
>>> test = ['red', 'blue']
>>> sample.extend(test)
>>> print(sample)
['earth', 'moon', 'red', 'blue']
'''

from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums) // 2):
            ans.extend([nums[2 * i + 1]] * nums[2 * i])
        return ans
    
ans = Solution()
print(ans.decompressRLElist([1, 2, 3, 4]))