class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        # Get the number of rows (m) and columns (n)
        m, n = len(matrix), len(matrix[0])
        
        # Initialize the left and right pointers for binary search
        left, right = 0, m * n - 1
        
        # Perform binary search
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            # Convert the middle index to the corresponding matrix element
            mid_value = matrix[mid // n][mid % n]
            
            # Check if the middle element is the target
            if mid_value == target:
                return True
            # If the middle element is less than the target, move the left pointer to mid + 1
            elif mid_value < target:
                left = mid + 1
            # If the middle element is greater than the target, move the right pointer to mid - 1
            else:
                right = mid - 1
                
        # If the target is not found, return False
        return False