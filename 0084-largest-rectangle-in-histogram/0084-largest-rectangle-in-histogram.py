class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair of (index, height)
        for i , h in enumerate(heights):
            idx = i
            if not stack:
                stack.append([i , h])
                continue
            while stack and stack[-1][1] > h:
                idx , he = stack.pop()
                maxArea = max(maxArea , (i - idx ) * he)
            stack.append([idx , h])

        while stack:
            idx , he = stack.pop()
            maxArea = max(maxArea , (i - idx + 1) * he) 
        return maxArea
