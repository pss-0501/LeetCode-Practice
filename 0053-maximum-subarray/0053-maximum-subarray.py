class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        sum1 = 0
        max1 = float('-inf')
        for i in range(len(nums)):
            sum1 += nums[i]
            if sum1 > max1:
                max1 = sum1
            if sum1 < 0:
                sum1 = 0

        return max1