# 617. Merge Two Binary Trees

'''
이 문제는 BFS로 풀 수 있습니다.
BFS는 Breath-First Search로, 위에서부터 같은 깊이를 다 훑은 후 다음 깊이를 탐색하는 방식입니다.

BFS를 푸는 방식은 아래와 같이 두가지로 나뉩니다.
- queue를 이용한 풀이
- recursive를 이용한 풀이
'''

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # QUEUE SOLUTION
    def mergeTreesQueue(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        elif not root2:
            return root1
        else:
            queue1 = deque([root1])
            queue2 = deque([root2])
            while queue1 and queue2:
                node1, node2 = queue1.popleft(), queue2.popleft()
                if node1 and node2: # node1과 node2가 모두 있을 경우만 진행하고 그렇지 않으면 다음으로 넘어감
                    node1.val += node2.val
                    if not node1.left and node2.left: # node1.left가 없고, node2.left만 있는 경우 node2.left.val을 추후 더해야 하므로 node1.left.val을 0인것으로 초기화
                        node1.left = TreeNode(0)
                    if not node1.right and node2.right:
                        node1.right = TreeNode(0)
                    queue1.append(node1.left)
                    queue1.append(node1.right)
                    queue2.append(node2.left)
                    queue2.append(node2.right)
            return root1
    
    # RECURSIVE SOLUTION
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        elif not root2:
            return root1
        else:
            ansRoot = TreeNode(root1.val + root2.val)
            ansRoot.left = self.mergeTrees(root1.left, root2.left)
            ansRoot.right = self.mergeTrees(root1.right, root2.right)
        return ansRoot
 
            