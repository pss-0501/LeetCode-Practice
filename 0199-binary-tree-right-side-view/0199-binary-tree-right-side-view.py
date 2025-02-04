# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.res = []
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, level):
        if node:
            if level == len(self.res):
                self.res.append(node.val)

            self.dfs(node.right, level + 1)
            self.dfs(node.left, level + 1)