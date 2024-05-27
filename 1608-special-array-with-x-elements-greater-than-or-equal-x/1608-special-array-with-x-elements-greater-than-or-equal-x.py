class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # a = len(nums)
        # for n in nums:
        #     if n < a:
        #         return -1
        # return -1
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            # x is the number of elements that are greater than or equal to nums[i]
            x = n - i
            
            # Check if there are exactly x numbers greater than or equal to x
            if nums[i] >= x and (i == 0 or nums[i-1] < x):
                return x
        
        # Check the edge case where x might be 0
        if nums[0] >= n:
            return n
        
        return -1