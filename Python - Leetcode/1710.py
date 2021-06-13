'''
1710. Maximum Units on a Truck

기존 leetcode 답안에서는 sort에 key를 넣어 따로 정렬 기준 세우는 걸 생각하지 못하여,
mergesort를 이용하여 답안을 제출했다.

Discuss를 보면서 sort를 이용해 쉽게 풀 수 있다는 것을 알게 되어 해당 내용을 남긴다.
* boxTypes.sort(key=lambda x: -x[1])
    - 위처럼 lambda를 쓰게 되면, 두번째 인자를 기준으로 정렬을 하며, -가 붙어 내림차순 정렬을 진행한다는 것이다.
'''

from typing import List

class Solution:              
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                ans += box * units
            else:
                ans += truckSize * units
                return ans
        return ans 