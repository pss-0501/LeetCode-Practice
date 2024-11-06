class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Brute Force
        nge = [-1] * len(nums)

        # arr = nums + nums

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, i + n):
                idx = j % n
                if nums[idx] > nums[i]:
                    nge[i] = nums[idx]
                    break

        return nge
