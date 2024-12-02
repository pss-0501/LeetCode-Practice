class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def count(k):
            if k < 0:
                return 0
            left = 0
            res = 0
            count = 0
            n = len(nums)

            for right in range(n):
                res += nums[right] % 2
                while res > k:
                    res -= nums[left] % 2
                    left += 1

                count = count + (right - left + 1)
            return count
        return count(k) - count(k - 1)