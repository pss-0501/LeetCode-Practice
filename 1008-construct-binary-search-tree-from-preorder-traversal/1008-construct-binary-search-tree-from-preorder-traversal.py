# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])

        def insert(node, value):
                if node.val > value:
                    if not node.left:
                        node.left = TreeNode(value)
                        return
                    insert(node.left, value)
                if node.val < value:
                    if not node.right:
                        node.right = TreeNode(value)
                        return
                    insert(node.right, value)
        for val in preorder[1:]:
            insert(root, val)
        return root
    
