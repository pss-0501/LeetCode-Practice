class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # when duplicate use set
        # Step 1: Create a new list to store unique elements
        unique_elements = []
        
        # Step 2: Iterate through the original list
        for num in nums:
            # Add the number to the new list if it is not already present
            if num not in unique_elements:
                unique_elements.append(num)
        
        # Step 3: Modify the original list to contain the unique elements
        for i in range(len(unique_elements)):
            nums[i] = unique_elements[i]
        
        # Return the number of unique elements
        return len(unique_elements)