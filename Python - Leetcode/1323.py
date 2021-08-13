# 1323. Maximum 69 Number

'''
replace함수의 인자로 넣을 수 있는 교체 횟수를 이용해 풀이하였다.
'''

class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6','9',1))

ans = Solution()
print(ans.maximum69Number(9999))
print(ans.maximum69Number(9669))
print(ans.maximum69Number(9996))