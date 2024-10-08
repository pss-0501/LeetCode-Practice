class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length
        