# 709. To Lover Case

'''
기존에는 ans = ""을 만들어서 for문을 돌때마다 각 char를 ans에 더하는 방식으로 풀이했다.
string의 경우 immutable한 변수로, string에 char을 더하면 새로운 string을 또 만들어내서 메모리 효율이 좋지 않았다.
이로 인해, string > list로 변환하고, 최종 결과를 join() 함수를 이용해 string화할 수 있게 하였다.
'''

class Solution:
    def toLowerCase(self, s: str) -> str:
        sList = list(s)
        for c in range(len(sList)):
            if ord(sList[c]) <= 90 and ord(sList[c]) >= 65:
                sList[c] = chr(ord(sList[c]) + 32)
            
        return "".join(sList)

ans = Solution()
print(ans.toLowerCase("Hello$abD"))