class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # return []
        
        # Optimal
        add_dict = {}
        n = len(nums)
        for i in range(n):
            rem = target - nums[i]
            if rem in add_dict:
                return [add_dict[rem],i]
            
            add_dict[nums[i]] = i

        return []

