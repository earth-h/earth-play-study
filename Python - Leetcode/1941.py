# 1941. Check if All Characters Have Equal Number of Occurrences

'''
Counter 클래스로 만든 dictionary의 value들로 set 만들어서 문제 풀이하기
'''
from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        if len(set(counter.values())) == 1:
            return True
        else:
            return False

ans = Solution()
print(ans.areOccurrencesEqual("aaabb"))