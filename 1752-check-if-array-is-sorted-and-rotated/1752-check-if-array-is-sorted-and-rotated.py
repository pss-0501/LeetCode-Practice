class Solution:
    def check(self, nums: List[int]) -> bool:
        a = len(nums)
        count_breaks = 0
        for i in range(1, a):
            if nums[i] < nums[i-1]:
                count_breaks += 1
                if count_breaks > 1:
                    return False
        if count_breaks == 1 and nums[-1] > nums[0]:
            return False

        return True