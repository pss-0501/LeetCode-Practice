class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        n = len(nums)
        right = n - 1

        while left <= right:
            mid = left + (right - left)
            if nums[mid] == target:
                return mid
            elif target < mid:
                left = mid + 1
            else:
                right = mid - 1

        return -1