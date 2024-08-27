class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_sum_dict = {0: 1}
        count = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            rem = prefix_sum - k
            if rem in prefix_sum_dict:
                count += prefix_sum_dict[rem]

            if prefix_sum in prefix_sum_dict:
                prefix_sum_dict[prefix_sum] += 1
            else:
                prefix_sum_dict[prefix_sum] = 1

        return count
            