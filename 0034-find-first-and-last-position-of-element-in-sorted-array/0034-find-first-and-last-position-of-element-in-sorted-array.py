class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1

        # Function to find the first occurrence (lower bound) of the target
        def lower_bound(nums, target):
            nonlocal first
            n = len(nums)
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    if nums[mid] == target:
                        first = mid  # Update first occurrence
                    high = mid - 1
                else:
                    low = mid + 1

        # Function to find the last occurrence (upper bound) of the target
        def upper_bound(nums, target):
            nonlocal last
            n = len(nums)
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    if nums[mid] == target:
                        last = mid  # Update last occurrence
                    low = mid + 1
                else:
                    high = mid - 1

        # Find the first and last occurrence of the target
        lower_bound(nums, target)
        upper_bound(nums, target)

        return [first, last] if first != -1 else [-1, -1]