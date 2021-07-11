# 1929. Concatenation of Array

'''
# 여러개의 리스트(List) 하나로 합치기
1. + 연산자를 사용하는 방법
array1 = [1]
array2 = [2]

array3 = array1 + array2
print(array3) # [1, 2]

2. extend() 함수를 사용하는 방법
array1 = [1]
array2 = [2]

array1.extend(array2)
print(array1) # [1, 2]
'''
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

answer = Solution()
print(answer.getConcatenation([1,2,1]))