class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nge = [-1] * len(nums)

        arr = nums + nums

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, i + n):
                if arr[j] > nums[i]:
                    nge[i] = arr[j]
                    break

        return nge
