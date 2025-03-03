# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if self.SameTree(root, subRoot):
            return True
        return self.SameTree(root.left, subRoot) or self.SameTree(root.right, subRoot)

    
    def SameTree(self, s, t):
        if not s and not t:
            return True

        if s and t and s.val == t.val:
            return (self.SameTree(s.left, t.left) and self.SameTree(s.right, t.right))

        if not s or not t or s.val != t.val:
            return False
            
        return False


