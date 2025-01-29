# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
        # if not root:
        #     return 0

        # queue = deque()
        # queue.append(root)
        # # res = []
        # count = 0

        # while queue:
        #     level = []
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         level.append(node.val)
                
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)

        #     count += 1   
        
        # return count

        # DFS
        r = 0
        l = 0
        if not root:
            return 0

        if root.left:
            l = self.maxDepth(root.left)

        if root.right:
            r = self.maxDepth(root.right)

        return 1 + max(l, r)

