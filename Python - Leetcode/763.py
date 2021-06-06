'''
763. Partition Labels

- 기존에 leetcode에서 작성한 코드와 방식은 유사하나,
python에서 제공하는 모듈을 사용하여 좀 더 효율성이 높은 코드로 재작성합니다.

* enumerate 사용
'''
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 하기에 주석처리 되어 있는 코드는 알파벳에 대해 모든 리스트를 만들어 for문을 사실상 한 번 더 돌았다.
        # 이를 방지하기 위해 enumerate을 사용하여 s에 등장하는 알파벳에 대해 key로 지정해서 가장 마지막에 나온 문자 위치를 value로 넣어주었다.
        sList = {k: v for v, k in enumerate(s)}
        # ex) {'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}
        ans = list()
        
        tmpLocation = 0
        # for문이 아닌 while을 사용하는 이유는?
        # for문의 경우 처음에 정해진 기준에 따라서 진행하기 때문에, 계속 max값이 바뀔 수 있는 경우 for문을 돌기 어렵다.
        # 따라서 while 사용
        while tmpLocation < len(s):
            maxLocation = sList[s[tmpLocation]]
            curLocation = tmpLocation
            while tmpLocation <= maxLocation:
                if sList[s[tmpLocation]] > maxLocation:
                    maxLocation = sList[s[tmpLocation]]
                tmpLocation += 1
            ans.append(maxLocation - curLocation + 1)
        '''
        #print(ord('z') - ord('a') + 1) # the number of alphabet
        #alphabet = [0 for _ in range(ord('z') - ord('a') + 1)]
        alphabet = [[0,0] for _ in range(26)]
        ans = list()
        
        for i in range(len(s)):
            strNum = ord(s[i]) - ord('a')
            if alphabet[strNum][0] == 0:
                alphabet[strNum][0] = i
            alphabet[strNum][1] = i
        
        curLocation = 0
        lastLocation = 0
        
        while curLocation < len(s): 
            strNum = ord(s[curLocation]) - ord('a')
            maxNum = alphabet[strNum][1]
            j = curLocation + 1
            while j <= maxNum:
                checkStrNum = ord(s[j]) - ord('a')
                if alphabet[checkStrNum][1] > maxNum:
                    maxNum = alphabet[checkStrNum][1]
                #print("curAlpha: ",s[j],"curLocation: ", curLocation, "maxNum: ", maxNum, "lastLocation: ",lastLocation)
                j += 1
            curLocation = maxNum + 1
            ans.append(curLocation - lastLocation)
            lastLocation = curLocation
        '''
        return ans

solution = Solution()
print(solution.partitionLabels("ababcbacadefegdehijhklij"))