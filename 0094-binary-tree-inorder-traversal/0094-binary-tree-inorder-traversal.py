# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        #inorder
        def dfs(node):
            if not node:
                return []
            
            if node.left is not None:
                dfs(node.left)
            arr.append(node.val)           
            if node.right is not None:
                dfs(node.right)

        dfs(root)
        return arr
            
            