class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxDeque = deque()  # Stores max values in the window
        minDeque = deque()  # Stores min values in the window
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            # Maintain maxDeque (decreasing order)
            while maxDeque and nums[maxDeque[-1]] < nums[right]:
                maxDeque.pop()
            maxDeque.append(right)
            
            # Maintain minDeque (increasing order)
            while minDeque and nums[minDeque[-1]] > nums[right]:
                minDeque.pop()
            minDeque.append(right)
            
            # If window is invalid, shrink it from the left
            while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
                left += 1
                # Remove elements from deques if they are out of the new window
                if maxDeque[0] < left:
                    maxDeque.popleft()
                if minDeque[0] < left:
                    minDeque.popleft()
            
            max_length = max(max_length, right - left + 1)
        
        return max_length