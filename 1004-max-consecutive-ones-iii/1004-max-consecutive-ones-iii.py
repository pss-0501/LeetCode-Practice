class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        flip = 0
        maxLen = 0
        n = len(nums)

        for right in range(n):
            if nums[right] == 0:
                flip += 1

            while flip > k:
                if nums[left] == 0:
                    flip -= 1
                left += 1

            if flip <= k:
                length = right - left + 1
                maxLen = max(maxLen, length)

        return maxLen
