class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0  # Minimum open brackets needed
        max_open = 0  # Maximum open brackets possible

        for char in s:
            if char == '(':
                min_open += 1  # We need one more open bracket
                max_open += 1  # Max count also increases
            elif char == ')':
                min_open = max(0, min_open - 1)  # Reduce min open, but not below 0
                max_open -= 1  # Reduce max open count
            else:  # '*' can act as '(', ')' or ''
                min_open = max(0, min_open - 1)  # Reduce min count (acting as ')')
                max_open += 1  # Increase max count (acting as '(')

            # If max_open drops below 0, too many ')' were found
            if max_open < 0:
                return False

        # If min_open is 0, we can successfully balance the string
        return min_open == 0
