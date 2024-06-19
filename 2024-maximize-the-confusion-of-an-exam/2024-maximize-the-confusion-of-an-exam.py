class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        AL = list(answerKey)
        n = len(AL)
        
        max_len = 0
        left = 0
        countT = 0
        countF = 0
        
        for right in range(n):
            if AL[right] == 'T':
                countT += 1
            else:
                countF += 1
            
            # Calculate the number of changes needed to make all characters in the window the same
            changes_needed = right - left + 1 - max(countT, countF)
            
            # If changes_needed exceeds k, shrink the window from the left
            if changes_needed > k:
                if AL[left] == 'T':
                    countT -= 1
                else:
                    countF -= 1
                left += 1
            
            # Update max_len with the length of the current valid window
            max_len = max(max_len, right - left + 1)
        
        return max_len

