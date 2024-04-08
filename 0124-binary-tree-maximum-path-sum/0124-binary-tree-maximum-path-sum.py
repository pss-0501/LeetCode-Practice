# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')  
        # Initialize to negative infinity to handle negative path sums

        def max_gain(node):
            if not node:
                return 0

            # Recursively get the maximum gain from the left and right subtrees
            left_gain = max(max_gain(node.left), 0)  # If the gain is negative, we choose 0 (do not include the subtree)
            right_gain = max(max_gain(node.right), 0)

            # Path sum including the current node and possibly both children
            price_newpath = node.val + left_gain + right_gain

            # Update the global maximum sum if the sum of the current path is greater
            self.max_sum = max(self.max_sum, price_newpath)

            # For the recursion return the maximum gain if we were to include this node in the path
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum