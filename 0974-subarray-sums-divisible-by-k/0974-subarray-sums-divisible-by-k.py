class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        remainder_count = {0: 1}
        
        for num in nums:
            current_sum += num
            remainder = current_sum % k
            if remainder < 0:  # Handle negative remainders
                remainder += k
            
            if remainder in remainder_count:
                count += remainder_count[remainder]
            
            if remainder in remainder_count:
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1
        
        return count