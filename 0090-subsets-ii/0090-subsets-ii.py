class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(i, res, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return


            # consider
            subset.append(nums[i])
            dfs(i + 1, res, subset)

            # dont consider
            subset.pop()
            # skip index to avoid duplicate
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, res, subset)

        dfs(0, res, subset)
        return res