# 1832. Check if the Sentence Is Pangram

'''
set을 이용하여, 집합자료형 생성하여 풀이

집합 자료형 특징
1. 중복을 허용하지 않는다.
2. 순서가 없다.

집합 자료형 초기화는 set() 함수나 중괄호({})를 이용할 수 있다.
'''

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26 # 소문자는 26자

ans = Solution()
print(ans.checkIfPangram("jwtucoucmdfwxxqnxzkaxoglszmfrcvjoiunqqausaxxaaijyqdqgvdnqcaihwilqkpivenpnekioyqujrdrovqrlxovcucjqzjsxmllfgndfprctxvxwlzjtciqxgsxfwhmuzqvlksyuztoetyjugmswfjtawwaqmwyxmvo"))