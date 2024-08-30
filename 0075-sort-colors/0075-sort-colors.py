class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Better sol
        c0 = 0
        c1 = 0
        c2 = 0

        for i in nums:
            if i == 0:
                c0 += 1
            elif i == 1:
                c1 += 1
            else:
                c2 += 1

        for i in range(c0):
            nums[i] = 0

        for j in range(c0,c0 + c1):
            nums[j] = 1

        for k in range(c0 + c1, c0 + c1 + c2):
            nums[k] = 2

        return nums
            
        # DNF Algo needs to be used
