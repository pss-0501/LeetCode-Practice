# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        def dfsToArray(root, res):
            if root:             
                dfsToArray(root.left, res)
                res.append(root.val)
                dfsToArray(root.right, res)

            return res

        arr = dfsToArray(root, [])
        # arr.sort()
        return arr[k - 1]