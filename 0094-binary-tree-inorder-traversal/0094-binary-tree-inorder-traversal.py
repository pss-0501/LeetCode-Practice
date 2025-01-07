# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = []
        node = root

        while stack or node:
            # Traverse the left subtree
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            res.append(node.val)

            node = node.right

        return res
