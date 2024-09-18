class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        n = len(nums)
        high = n - 1
        min1 = nums[0]
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= nums[high]:
                min1 = min(min1, nums[mid])
                low = mid + 1
            else:
                min1 = min(min1, nums[mid])
                high = mid - 1

        return min1
