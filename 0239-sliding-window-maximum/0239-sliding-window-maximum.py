class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        result = []
        for i in range(len(nums) - k + 1):
            result.append(max(nums[i:i + k]))
        return result