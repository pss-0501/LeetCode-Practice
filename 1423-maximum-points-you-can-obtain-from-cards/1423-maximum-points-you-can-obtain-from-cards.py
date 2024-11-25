class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MaxSum = 0
        Lsum = 0
        for i in range(k):
            Lsum = Lsum + nums[i]
        
        MaxSum = Lsum


        Rsum = 0
        rightIndex = n - 1
        for i in range(k-1, -1, -1):
            Lsum = Lsum - nums[i]
            Rsum = Rsum + nums[rightIndex]
            rightIndex -= 1
        
            MaxSum = max(MaxSum, Lsum + Rsum)

        return MaxSum