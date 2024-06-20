class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
    
    # Function to check if it is possible to place m balls with at least given minimum distance
        def canPlaceBalls(min_dist):
            count = 1  # Place the first ball in the first basket
            last_position = position[0]  # Position of the last placed ball
            
            for i in range(1, len(position)):
                if position[i] - last_position >= min_dist:
                    count += 1
                    last_position = position[i]
                    if count == m:  # All balls have been placed successfully
                        return True
            return False
        
        # Binary search for the largest minimum distance
        low = 1
        high = position[-1] - position[0]
        best = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlaceBalls(mid):
                best = mid  # Update best to the current mid if we can place all balls
                low = mid + 1  # Try for a larger distance
            else:
                high = mid - 1  # Try for a smaller distance
        
        return best