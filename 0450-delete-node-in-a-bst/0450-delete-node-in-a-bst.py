# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        
        def min_val(node):
            while node.left is not None:
                node = node.left
            return node
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                sub_tree = min_val(root.right).val
                root.val = sub_tree
                root.right = self.deleteNode(root.right, sub_tree)

        return root
