# 804. Unique Morse Code Words

'''
answer는 각각 unique해야 합니다.
처음에는 list로 구하면서 해당 값이 기존 list에 없으면 추가하는 형식으로 진행했는데,
항상 unique해야 하는 set(집합)을 이용하는 방법으로 수정했습니다.
'''
from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpha = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = set()

        for word in words:
            ans.add("".join(alpha[ord(c) - 97] for c in word))
        
        return len(ans)

ans = Solution()
print(ans.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))