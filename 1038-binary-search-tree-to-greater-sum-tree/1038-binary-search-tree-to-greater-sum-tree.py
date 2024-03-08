# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        curSum = 0

        def DFS(node):
            if not node:
                return
            nonlocal curSum
            DFS(node.right)
            curSum += node.val
            node.val = curSum
            DFS(node.left)

        DFS(root)
        return root 