# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def DFS(node, curSum):
            if not node:
                return False
                
            curSum += node.val
            if node.left == None and node.right == None:
                return curSum == targetSum

            return (DFS(node.left, curSum) or DFS(node.right, curSum))

        return DFS(root,0)

            