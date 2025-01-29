# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Brute Force On^2
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True

    #     left_height = self.height(root.left)
    #     right_height = self.height(root.right)

    #     if abs(left_height - right_height) > 1:
    #         return False

    #     return self.isBalanced(root.left) and self.isBalanced(root.right)

    # def height(self, root):
    #     if not root:
    #         return 0
        
    #     left_height = self.height(root.left)
    #     right_height = self.height(root.right)

    #     return max(left_height, right_height) + 1

    # Optimise
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) != -1

    def height(self, node):
        if not node:
            return 0

        left_height = self.height(node.left)
        if left_height == -1:
            return -1  # Left subtree is unbalanced

        right_height = self.height(node.right)
        if right_height == -1:
            return -1  # Right subtree is unbalanced

        if abs(left_height - right_height) > 1:
            return -1  # Current tree is unbalanced

        return max(left_height, right_height) + 1