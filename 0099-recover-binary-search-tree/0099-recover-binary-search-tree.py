# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        in_order = []

        def dfsInorder(node):
            if not node:
                return
            dfsInorder(node.left)
            in_order.append(node) 
            dfsInorder(node.right)

        dfsInorder(root)

        first = second = None
        for i in range(len(in_order) - 1):
            if in_order[i].val > in_order[i + 1].val:
                if not first:
                    first = in_order[i] 
                second = in_order[i + 1]  

        if first and second:
            first.val, second.val = second.val, first.val

