# 1486. XOR Operation in an Array

'''
brute force로 풀 수 있지만, 아래와 같이 규칙성을 찾아 풀 수도 있다.
https://leetcode.com/problems/xor-operation-in-an-array/discuss/699141/Visual-Solution-Python-or-O(1)-Time-or-O(1)-Space

start = 0/1

n % 4 == 1 => nums[n - 1]
n % 4 == 2 => 2
n % 4 == 3 => nums[n - 1] ^ 2
n % 4 == 0 => 0

start = 2/3

n % 4 == 1 => nums[0]
n % 4 == 2 => nums[n - 1] ^ nums[0]
n % 4 == 3 => nums[0] ^ 2
n % 4 == 0 => nums[n - 1] ^ nums[0] ^ 2
'''

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        if start % 4 <= 1:
            if n % 4 == 1:
                return start + (n - 1) * 2
            elif n % 4 == 2:
                return 2
            elif n % 4 == 3:
                return (start + (n - 1) * 2) ^ 2
            else:
                return 0
        else:
            if n % 4 == 1:
                return start
            elif n % 4 == 2:
                return (start + (n - 1) * 2) ^ start
            elif n % 4 == 3:
                return start ^ 2
            else:
                return (start + (n - 1) * 2) ^ start ^ 2

ans = Solution()
print(ans.xorOperation(5, 0))