# 589. N-ary Tree Preorder Traversal

'''
pre-order Traversal을 recursive형식이 아닌, iterative로 푸는 방식
'''
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack = [root]
        ans = []

        while stack:
            curNode = stack.pop()
            ans.append(curNode.val)
            stack.extend(curNode.children[::-1])
        
        return ans