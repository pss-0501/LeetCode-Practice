# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None
        res = []
        def DFS(node):
            # if node is None:
            #     return
            res.append(node.val)
            if node.left is not None:
                DFS(node.left)
            if node.right is not None:
                DFS(node.right)
        DFS(root)    
        return res
            