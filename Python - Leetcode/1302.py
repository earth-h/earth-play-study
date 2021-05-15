# 1302. Deepest Leaves Sum
'''
DFS로 가장 깊은 곳까지 들어가서 자식 노드 없는 노드들의 합 체크
이 때, max Depth일 때만 필요하기 때문에
max Depth를 class의 멤버변수로 두고 사용
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxDepth = 0
    maxSum = 0
    def dfs(self, root: TreeNode, currentDepth):
        if root.left is None and root.right is None:
            if self.maxDepth < currentDepth:
                self.maxDepth = currentDepth
                self.maxSum = root.val
            elif self.maxDepth == currentDepth:
                self.maxSum += root.val
            return
        
        if root.left is not None:
            self.dfs(root.left, currentDepth+1)
        if root.right is not None:
            self.dfs(root.right, currentDepth+1)

    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        #depth = [0 for _ in range(10000)] # 1 <= node count <= 10000
        currentDepth = 0
        self.maxDepth = 0
        self.maxSum = 0
        
        self.dfs(root, 0)
        
        return self.maxSum