class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # res = []
        # count  = 0
        # for i in nums:
        #     if i not in res:
        #         res.append(i)
        #         continue
        #     i += 1
        #     count += 1
        # return count
        if not nums:
            return 0
        
        # Sort the nums array
        nums.sort()
        
        # Initialize the count of moves
        moves = 0
        
        # Traverse the sorted array and ensure all elements are unique
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                 # Calculate the increment needed to make the current element unique
                increment = nums[i - 1] - nums[i] + 1
                # Update the current element
                #nums[i] += increment
                # Add the increment to the total moves count
                moves += increment
        
        return moves


