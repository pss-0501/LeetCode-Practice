# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        res = []
        
        def dfs(node):
            if not node:
                return res.append('N')
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)
        
        return dfs(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        data_list = data.split(',')

        def dfs(nodes_list):
            val = nodes_list.pop(0)
            if val == 'N':
                return None
            node = TreeNode(int(val))
            node.left = dfs(nodes_list)
            node.right = dfs(nodes_list)
            return node
                
        root = dfs(data_list)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))