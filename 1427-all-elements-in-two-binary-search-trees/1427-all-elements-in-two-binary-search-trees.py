# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        def DFS(node):
            if node:
                DFS(node.left)
                res.append(node.val)
                DFS(node.right)
        DFS(root1)
        DFS(root2)

        return sorted(res)