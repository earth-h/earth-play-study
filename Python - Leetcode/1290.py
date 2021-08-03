# 1290. Convert Binary Number in a Linked List to Integer

'''
bit operator 사용
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head != None:
            ans = (ans << 1) + head.val
            head = head.next
        return ans

a = ListNode(1)
b = ListNode(0, a)
c = ListNode(1, b)
ans = Solution()
print(ans.getDecimalValue(c))
