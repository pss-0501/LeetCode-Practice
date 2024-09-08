class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Better Solution
        nums.sort()
        longt = 0
        count = 0
        prev = lastSmaller = float('-inf')

        for i in range(len(nums)):
            if nums[i] - 1 == prev:
                prev = nums[i]
                count += 1
            elif nums[i] != prev:
                count = 1
                prev = nums[i]
            longt = max(count, longt)
        return longt


        # Brute Solution
    #     longt = 0
    #     n = len(nums)
    #     for i in range(n):
    #         count = 1
    #         targ = nums[i]
    #         while(self.ls(nums, targ + 1) == True):
    #             count += 1
    #             targ += 1
    #         longt = max(longt, count)
    #     return longt

    # def ls(self, nums, target):
    #     for i in range(len(nums)):
    #         if nums[i] == target:
    #             return True
    #     return False