# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left, right = root, root
        l_h, r_h = 0,0
        while left != None:
            l_h += 1
            left = left.left

        while right != None:
            r_h += 1
            right = right.right

        if l_h == r_h:
            return (2 ** l_h) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


        