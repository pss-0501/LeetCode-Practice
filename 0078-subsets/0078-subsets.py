class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset, currsets = [], []

        def helper(i, nums, subset, currsets):
            # Correcting the condition to check if we've gone through all elements
            if i >= len(nums):
                subset.append(currsets.copy())  # Add a copy of the current subset
                return

            # Decision to include nums[i]
            currsets.append(nums[i])
            helper(i + 1, nums, subset, currsets)
            currsets.pop()  # Backtrack to remove the last element added

            # Decision to not include nums[i]
            helper(i + 1, nums, subset, currsets)

        helper(0, nums, subset, currsets)
        return subset