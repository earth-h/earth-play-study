# 1844. Replace All Digits with Characters

'''
기존 풀이의 경우, string을 계속 +하는 형식이라, 메모리 효율이 안 좋았다.
(string의 경우 immutable<값이 변하지 않음>해서 계속 새로 생성함)

그래서, ans를 list에 넣고 마지막에 join 함수를 통해 string화 했다.
'''

class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = []
        for i in range(len(s) // 2):
            ans.append(s[2 * i] + chr(ord(s[2 * i]) + int(s[2 * i + 1])))
        if len(s) % 2 == 1:
            ans.append(s[-1])
        return "".join(ans)

ans = Solution()
print(ans.replaceDigits("a1b2c3d4e"))