# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        res = []

        def dfs(node):
            if node.left is not None:
                dfs(node.left)
            res.append(node.val)
            if node.right is not None:
                dfs(node.right)

        dfs(root)
        for i in range(1,len(res)):
            if res[i - 1] != res[i]:
                return False

        return True