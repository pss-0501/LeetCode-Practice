class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        flips = 0
        maxLen = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                flips += 1

            while flips > k:
                if nums[left] == 0:
                    flips -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen

            
