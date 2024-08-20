class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        temp = []
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])
        
        for k in range(len(temp)):
            nums[k] = temp[k]
        
        for j in range(len(temp), len(nums)):
            nums[j] = 0