# Shuffle String

'''
기존 풀이와 별반 다르지 않으나, join()을 이용하여 쉽게 문자열 합치는 걸 이용해보고자 한다.

join 함수는 리스트의 문자열을 합치는 역할을 한다.

예) 리스트들 사이에 아무것도 넣지 않고 합칠 경우
str = "Hello my name is earth"
split_str = str.split()
print(split_str) #['Hello', 'my', 'name', 'is', 'earth']
join_str = "".join(split_str)
print(join_str) #Hellomynameisearth
'''
from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_s = list()
        for i in s:
            new_s.append(i)
        
        for i in range(len(indices)):
            new_s[indices[i]] = s[i] 
        
        return "".join(new_s)

ans = Solution()
print(ans.restoreString("codeleet", [4,5,6,7,0,2,1,3]))