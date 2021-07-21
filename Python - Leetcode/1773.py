# 1773. Count Items Matching a Rule

'''
for문과 if문을 한 줄로 쓰면서, sum 함수를 써볼 수 있는 문제이다.
'''

from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
            ruleKeyDict = {"type": 0, "color": 1, "name": 2}

            return sum(1 for item in items if item[ruleKeyDict[ruleKey]] == ruleValue)

ans = Solution()
print(ans.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone"))