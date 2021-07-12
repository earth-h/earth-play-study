# 1431. Kids With the Greatest Number of Candies

'''
python if문과 for문 한 줄로 쓰기를 이용해서 구현했으나,
좀 더 간결하게 작성하도록 수정한 버전입니다.

[ 기존 버전 ]
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)

        return [True if i + extraCandies >= maxCandies else False for i in candies]

if/else문의 결과를 따로 True, False로 나타내줄 필요가 없는게, 
반환하는 답변이 bool형식이기 때문에 if문 결과의 True, False가 알아서 반환되므로
따로 반환값을 작성해주지 않아도 됩니다.
'''

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)

        return [i + extraCandies >= maxCandies for i in candies]

ans = Solution()
print(ans.kidsWithCandies([2, 3, 5, 1, 3], 3))