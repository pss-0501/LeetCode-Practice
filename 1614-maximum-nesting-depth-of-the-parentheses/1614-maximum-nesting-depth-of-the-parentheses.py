class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = []
        count = 0

        for c in s:
            if c == '(':
                stack.append(c)
                count = max(count, len(stack))
            elif c == ')':
                stack.pop()
        
        return count

        