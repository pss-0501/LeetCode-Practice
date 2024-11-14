class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sum1 = 0
        n = len(nums)
        for i in range(n):
            small = nums[i]
            large = nums[i]
            for j in range(i + 1, n):
                large = max(nums[j], large)
                small = min(nums[j], small)
                sum1 = sum1 + (large - small)

        return sum1