# 1436. Destination City

'''
차집합을 이용한 풀이
'''

from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return (set([path[1] for path in paths]) - set([path[0] for path in paths])).pop()

ans = Solution()
print(ans.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))