# 905. Sort Array By Parity

'''
기존에 풀었던 방식은 리스트를 even과 odd로 나누어 2개의 리스트로 생성한 뒤 해당 리스트를 합쳤습니다.
이 경우, 속도는 빠르나 메모리를 추가로 사용하는 부분이 있어 swap하는 방식으로 하여 메모리를 추가 사용하지 않도록 했습니다.

추가적으로, python에서 swap은 num[A]와 num[B]를 swap한다고 할 때, temp 변수 필요없이 num[A], num[B] = num[B], num[A]로 가능합니다.
'''
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums

ans = Solution()
print(ans.sortArrayByParity([3, 1, 2, 4]))