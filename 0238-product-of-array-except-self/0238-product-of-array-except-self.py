class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = [1] * n

        pf = 1
        for i in range(n):
            prod[i] = pf
            pf *= nums[i]

        sf = 1
        for i in range(n-1, -1, -1):
            prod[i] *= sf
            sf *= nums[i]

        return prod