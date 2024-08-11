class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(per):
            if len(per) == len(nums):
                ans.append(per.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in per:
                    continue
                per.append(nums[i])
                backtrack(per)
                per.pop()

        backtrack([])
        return ans