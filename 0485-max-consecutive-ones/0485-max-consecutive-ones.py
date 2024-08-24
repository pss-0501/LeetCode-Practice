class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        max1 = 0
        for i in nums:
            if i == 1:
                ones += 1
                max1 = max(max1, ones)
            elif i == 0:
                ones = 0

        return max1