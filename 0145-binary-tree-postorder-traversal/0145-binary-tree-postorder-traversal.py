# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # DFS

        # res = []
        # if not root:
        #     return []

        # if root.left:
        #     res.extend(self.postorderTraversal(root.left))
        # if root.right:
        #     res.extend(self.postorderTraversal(root.right))

        # res.append(root.val)

        # return res

        # Iterative 2 stack

        res = []
        stack1 = []
        stack2 = []

        stack1.append(root)

        while stack1:
            node = stack1.pop()
            if node:
                stack2.append(node)

                # Push left and right children of the node to stack1
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)

        # Collect nodes from stack2 in reverse order
        while stack2:
            node = stack2.pop()
            res.append(node.val)

        return res