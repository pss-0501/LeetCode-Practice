class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # BF
        
        # res = float('-inf')
        # 
        # left = 0
        # right = k
        # while right <= n:
        #     avg = sum(nums[left:right]) / k
        #     res = max(res, avg)
        #     left += 1
        #     right += 1

        # return res


        # Optimise

        n = len(nums)
        current_sum = sum(nums[:k])
        max_sum = current_sum

        for i in range(k, n):
            current_sum = current_sum + nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)

        return max_sum/k
