class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Brute Force

        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # for i in range(n):
        #     if i == 0:
        #         if nums[i] != nums[i + 1]:
        #             return nums[i]
        #     elif i == n - 1:
        #         if nums[i] != nums[i - 1]:
        #             return nums[i]
        #     else:
        #         if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
        #             return nums[i]

        # Optimise
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n-1]
        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            # left side even,odd
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                low = mid + 1
            else:
                high = mid - 1

        return -1
            
