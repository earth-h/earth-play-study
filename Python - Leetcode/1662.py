#1662. Check If Two String Arrays are Equivalent

'''
generator를 활용한 풀이
- yield를 이용하여 word1과 word2의 알파벳을 하나씩 호출하여 동일한지 확인

> yield None이 존재해야 하는 이유는, word1과 word2의 자리수가 다를 때 오류가 나는 것을 방지하기 위함

# 풀이 1
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

generator를 사용한 풀이는, 풀이 1은 시간 복잡도가 O(n + m)인 반면, 풀이 2는 시간 복잡도가 O(min(n, m))입니다.
'''
# 풀이 2

from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for a, b in zip(self.generator(word1), self.generator(word2)):
            if a != b:
                return False
        return True

    def generator(self, word: List[str]):
        for s in word:
            for j in s:
                yield j
        yield None

ans = Solution()
print(ans.arrayStringAreEqual(["ab", "c"], ["a","b"]))