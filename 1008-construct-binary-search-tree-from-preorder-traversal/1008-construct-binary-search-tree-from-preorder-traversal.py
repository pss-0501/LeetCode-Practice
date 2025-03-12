# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])

        def insert_into_bst(node, val):
            if not node:
                return TreeNode(val)
            if val < node.val:
                node.left = insert_into_bst(node.left, val)
            else:
                node.right = insert_into_bst(node.right, val)
            return node

        for val in preorder[1:]:
            insert_into_bst(root, val)
        
        return root