# 1684. Count the Number of Consistent Strings

'''
기존에는 allowed를 dict에 넣어서 구했지만,
allowed안에 있는 값인지 체크하는 것은 allowed 값을 각각 dict의 key로 볼 수도 있지만,
집합으로 생성하는 것이 더 빠르기 때문에 집합으로 풀어보았습니다.
'''

from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        cnt = 0

        for word in words:
            for c in word:
                if c not in allowed:
                    cnt += 1
                    break

        return len(words) - cnt

ans = Solution()
print(ans.countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))
print(ans.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))