class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # BF

        # res = 0
        # left = 0
        # n = len(nums)
        # for i in range(n):
            
        #     total = 0
        #     for j in range(i, n):
        #         total += nums[j]
        #         if total == goal:
        #             res += 1

        # return res

        # OP
        def atMost(goal):

            if goal < 0:
                return 0

            left = 0
            res = 0
            count = 0
            n = len(nums)

            for right in range(n):
                res += nums[right]
                while res > goal:
                    res -= nums[left]
                    left += 1

                count = count + (right - left + 1)

            return count

        return atMost(goal) - atMost(goal - 1)