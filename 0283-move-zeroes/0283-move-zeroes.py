class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # Brute Force
        # temp = []
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         temp.append(nums[i])
        
        # for k in range(len(temp)):
        #     nums[k] = temp[k]
        
        # for j in range(len(temp), len(nums)):
        #     nums[j] = 0

        # Optimise
        l = 0
        r = l + 1
        while r < len(nums):
            if nums[r] != 0:
                # Swap if `l` is not equal to `r` to avoid redundant swaps
                if l != r:
                    nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
