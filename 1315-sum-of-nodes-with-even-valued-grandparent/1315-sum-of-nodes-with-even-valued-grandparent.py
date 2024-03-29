# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node):
            if not node:
                return 0
            nonlocal ans
            if node.val%2 == 0:
                if node.left and node.left.left:
                    ans += node.left.left.val
                if node.left and node.left.right:
                    ans += node.left.right.val
                if node.right and node.right.left:
                    ans += node.right.left.val
                if node.right and node.right.right:
                    ans += node.right.right.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans

            
