class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def calThres(nums, i):
            sum1 = 0
            for n in nums:
                sum1 += math.ceil(n/i)
            return sum1

        low = 1
        high = max(nums)
        while low <= high:
            mid = (low + high) // 2
            sum1 = calThres(nums, mid)
            if sum1 <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans