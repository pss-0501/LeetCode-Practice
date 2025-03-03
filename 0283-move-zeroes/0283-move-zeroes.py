class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = []
        for i in nums:
            if i != 0:
                tmp.append(i)

        for i in range(len(tmp)):
            nums[i] = tmp[i]

        for i in range(len(tmp), len(nums)):
            nums[i] = 0 

        # n = len(nums)
        # l = 0
        # r = l
        # while r < n:      
        #     if nums[r] != 0:
        #         if l != r:
        #             nums[l], nums[r] = nums[r], nums[l]
        #         l += 1
        #     r += 1
