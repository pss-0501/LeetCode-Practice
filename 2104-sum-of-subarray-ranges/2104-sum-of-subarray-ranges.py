class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # Brute Force
        # sum1 = 0
        # n = len(nums)
        # for i in range(n):
        #     small = nums[i]
        #     large = nums[i]
        #     for j in range(i + 1, n):
        #         large = max(nums[j], large)
        #         small = min(nums[j], small)
        #         sum1 = sum1 + (large - small)

        # return sum1

        # Optimse
        def max_sum(nums):
            stack = []
            res = 0
            n = len(nums)

            for i in range(n + 1):
                while stack and (i == n or nums[stack[-1]] < nums[i]):
                    j = stack.pop()
                    left = j - (stack[-1] if stack else -1)
                    right = i - j
                    res += nums[j] * left * right
                stack.append(i)
            return res

        def min_sum(nums):
            stack = []
            res = 0
            n = len(nums)

            for i in range(n + 1):
                while stack and (i == n or nums[stack[-1]] > nums[i]):
                    j = stack.pop()
                    left = j - (stack[-1] if stack else -1)
                    right = i - j
                    res += nums[j] * left * right
                stack.append(i)
            
            return res

        max1 = max_sum(nums)
        min1 = min_sum(nums)
        return max1 - min1
        