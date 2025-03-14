# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        suck = None

        curr = root
        while curr:
            if curr.val > p.val:
                suck = curr
                curr = curr.left

            else:
                curr = curr.right

        return suck