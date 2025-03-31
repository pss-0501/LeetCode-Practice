class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        currset = []

        def recur(index):
            if index >= len(nums):
                res.append(currset.copy())
                return

            # include
            currset.append(nums[index])
            recur(index + 1)

            # dont include
            currset.pop()
            recur(index + 1)

        recur(0)
        return res
        