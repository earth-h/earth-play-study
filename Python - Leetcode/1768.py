# 1768. Merge Strings Alternately

'''
두 가지 string을 하나로 합치되, 번갈아서 값을 넣어야 합니다.
두 string의 길이는 각각 다를 수 있으므로, zip()이 아닌 zip_longest()를 사용합니다.
'''

from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))

ans = Solution()
print(ans.mergeAlternately("ab", "pqrs"))