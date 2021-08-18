# 1370. Increasing Decreasing String

'''
collections.Counter 클래스를 활용한 데이터 개수 세어 문제 풀이
'''

from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        # counter: data 세어서 만든 dic, ans: answer용 list, asc: sort 기준
        counter, ans, asc = Counter(s), [],  True
        while counter: # dicionary에 데이터가 남아있는 동안 계속 진행
            for c in sorted(counter) if asc else reversed(sorted(counter)):
                ans.append(c)
                counter[c] -= 1
                if counter[c] == 0:
                    del counter[c]
            asc = not asc
        return "".join(ans)

ans = Solution()
print(ans.sortString("aaaabbbbcccc"))