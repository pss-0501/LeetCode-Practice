class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # when duplicate use set
        unique_elements = list(set(nums))
        
        # Modify nums in-place to contain only unique elements
        nums[:] = unique_elements
        
        return len(unique_elements)