class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(0)
        for i, num in enumerate(nums):
            if i != num:
                return i
        return len(nums)