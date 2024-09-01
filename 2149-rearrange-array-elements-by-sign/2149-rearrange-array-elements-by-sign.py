class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Brute Force
        # pos = []
        # neg = []
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         pos.append(nums[i])
        #     elif nums[i] < 0:
        #         neg.append(nums[i])

        # n = len(nums) // 2
        # nums = []

        # for i in range(n):
        #     nums.append(pos[i])
        #     nums.append(neg[i])

        # return nums

        # Optimise
        pos = 0
        neg = 1
        ans = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                ans[pos] = nums[i]
                pos += 2
            else:
                ans[neg] = nums[i]
                neg += 2

        return ans
