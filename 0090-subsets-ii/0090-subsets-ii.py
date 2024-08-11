class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset, curset = [],[]

        def helper(i, nums, curset, subset):
            if i >= len(nums):
                subset.append(curset.copy())
                return
            
            # include num[i]
            curset.append(nums[i])
            helper(i + 1, nums, curset, subset)
            curset.pop()

            # not include
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i+1, nums, curset, subset)

        helper(0, nums, curset, subset)
        return subset 