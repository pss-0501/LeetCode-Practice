class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        current_position = 1
        direction = 1  # 1 means forward, -1 means backward
        
        for _ in range(time):
            current_position += direction
            
            # Change direction if the ends are reached
            if current_position == n:
                direction = -1
            elif current_position == 1:
                direction = 1
                
        return current_position