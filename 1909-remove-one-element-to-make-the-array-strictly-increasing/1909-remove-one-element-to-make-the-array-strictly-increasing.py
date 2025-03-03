class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        res = []
        change = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                if change > 0:
                    return False
                change += 1

            #  for example 2
                if i - 2 >= 0 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]  # Modify nums[i] to nums[i - 1]

        return True