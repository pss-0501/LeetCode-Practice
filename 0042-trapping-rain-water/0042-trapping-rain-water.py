class Solution:
    def trap(self, height: List[int]) -> int:
        # optimise solution, 2 pointer
        total = 0
        leftMax = 0
        rightMax = 0

        n = len(height)
        left = 0
        right = n - 1

        while left < right:
            if height[left] <= height[right]:
                if leftMax > height[left]:
                    total += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1

            else:
                if rightMax > height[right]:
                    total += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1

        return total
