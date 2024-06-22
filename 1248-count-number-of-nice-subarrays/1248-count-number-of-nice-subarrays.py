class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        odd_count = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        for num in nums:
            # Increment odd_count if the number is odd
            if num % 2 == 1:
                odd_count += 1
            
            # Check if there is a prefix sum that would result in k odd numbers
            if odd_count - k in prefix_sum:
                count += prefix_sum[odd_count - k]
            
            # Update the prefix sums with the current odd_count
            prefix_sum[odd_count] += 1
    
        return count