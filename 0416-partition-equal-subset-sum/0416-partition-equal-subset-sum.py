class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        half = total // 2
        dp = set([0])
        for num in nums:
            new_dp = set(dp)  # Make a copy of the current dp set.
            for s in dp:
                new_sum = s + num
                if new_sum == half:
                    return True
                elif new_sum < half:
                    new_dp.add(new_sum)
            dp = new_dp

        return False


