class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Dictionary to keep track of the count of characters in t
        t_count = Counter(t)
        current_count = defaultdict(int)
        
        # Initialize the window pointers and the minimum length variables
        start = 0
        min_len = float("inf")
        min_start = 0
        required = len(t_count)
        formed = 0
        l = 0
        
        for r in range(len(s)):
            # Add current character to the window
            current_count[s[r]] += 1
            
            # If current character's count in window matches its count in t
            if s[r] in t_count and current_count[s[r]] == t_count[s[r]]:
                formed += 1
            
            # Contract the window until it's no longer valid
            while l <= r and formed == required:
                # Update the minimum window
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_start = l
                
                # Remove the leftmost character from the window
                current_count[s[l]] -= 1
                if s[l] in t_count and current_count[s[l]] < t_count[s[l]]:
                    formed -= 1
                
                # Move the left pointer to the right
                l += 1
        
        # Return the minimum window substring if found, else return empty string
        if min_len == float("inf"):
            return ""
        else:
            return s[min_start:min_start + min_len]