class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unq_terms = set()
        
        # Iterate over the array and add non-zero elements to the set
        for num in nums:
            if num != 0:
                unq_terms.add(num)
        
        # The number of unique non-zero elements is the result
        return len(unq_terms)