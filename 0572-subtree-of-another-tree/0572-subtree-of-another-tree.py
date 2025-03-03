class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        # Check if current node's subtree is identical to subRoot
        if self.SameTree(root, subRoot):
            return True
        # Otherwise, continue to search in left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def SameTree(self, s, t):
        # If both trees are None, they are the same
        if not s and not t:
            return True
        # If one is None or values are different, they are not the same
        if not s or not t or s.val != t.val:
            return False
        # Recursively check both left and right subtrees
        return self.SameTree(s.left, t.left) and self.SameTree(s.right, t.right)
