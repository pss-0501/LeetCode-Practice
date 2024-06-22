class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stack = []
        maxsum = counter = 0

        for i in s:
            if i not in stack:
                stack.append(i)
                counter += 1
            else:
                counter = 0
                while stack:
                    stack.pop()
            maxsum = max(counter, maxsum)

        return maxsum
            

        