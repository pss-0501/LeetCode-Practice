# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # def preorder_traversal(node):
        #     if node is None:
        #         return []
        #     return [node] + preorder_traversal(node.left) + preorder_traversal(node.right)
        
        # # Perform preorder traversal
        # preorder_nodes = preorder_traversal(root)
        
        # # Merge nodes to the right and make left null
        # for i in range(len(preorder_nodes) - 1):
        #     preorder_nodes[i].left = None
        #     preorder_nodes[i].right = preorder_nodes[i + 1]
        

        ######
        if not root:
            return []

        res = []
        def dfs(root):
            res.append(root)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        
        dfs(root)

        for i in range(len(res) - 1):
            res[i].left = None
            res[i].right = res[i + 1]
            
                
            