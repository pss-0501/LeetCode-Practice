# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.res = []
        
        def dfs(node, level):
            if node:
                if level == len(self.res):
                    # We only add the first node we encounter at each level,
                    # which, due to our traversal, will be the rightmost node.
                    self.res.append(node.val)
                # First go right, then left, ensuring we see rightmost nodes first.
                dfs(node.right, level + 1)
                dfs(node.left, level + 1)
                
        dfs(root, 0)
        return self.res    