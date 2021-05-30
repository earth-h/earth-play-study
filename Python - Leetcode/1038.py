'''
1038. Binary Search Tree to Greater Sum Tree

BST(Binary Search Tree)의 경우 아래와 같은 속성을 갖습니다.
- 왼쪽 서브 트리 노드 값 < 자기 자신
- 오른쪽 서브 트리 노드 값 > 자기 자신

Tree를 순회(traverse)하는 방법 중 in-order-traversal 활용
- in_order_traversal은 왼쪽 서브 트리 -> 자기 자신 -> 오른쪽 서브 트리 순으로 순회한다.
    - 즉, 제일 작은 값부터 순회한다고 보면 된다.

이 문제의 경우, Greater Sum Tree를 만들어야 해서, 자신보다 큰 노드들을 모두 더해야 한다.
따라서, in_order_traversal을 반대로 시행해보면 된다.
    - 오른쪽 서브 트리 -> 자기 자신 -> 왼쪽 서브 트리 순서
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def reverse_in_order_traversal(node: TreeNode, greaterSum: int) -> int:
            if node is None:
                return greaterSum
            greaterSum = reverse_in_order_traversal(node.right, greaterSum) # right
            '''
            메모리 사용을 줄여보고자 임시 변수 제거
            '''
            #curNode = node.val # tmp variable(current node value)
            node.val += greaterSum
            #greaterSum += curNode
            greaterSum = reverse_in_order_traversal(node.left, node.val) # left
            return greaterSum
            
        reverse_in_order_traversal(root, 0)
     
        return root