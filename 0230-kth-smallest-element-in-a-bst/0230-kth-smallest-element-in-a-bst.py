# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []

        def DFS(node):  #inorder
            if node is None:
                return
            DFS(node.left)
            self.res.append(node.val)
            DFS(node.right)

        DFS(root)
        return self.res[k - 1]      # index start from 0