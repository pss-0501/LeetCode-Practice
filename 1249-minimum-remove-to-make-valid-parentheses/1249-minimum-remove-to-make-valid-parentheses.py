class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        new_str = ''
        open_count = 0  # Count of unmatched opening parentheses
        for char in s:
            if char == '(':
                open_count += 1
                new_str += char
            elif char == ')':
                if open_count > 0:  # There's an opening parenthesis to match this closing one
                    open_count -= 1
                    new_str += char
                # If open_count is 0, this closing parenthesis is excess and not added
            else:  # Any other character is added as is
                new_str += char

        final_str = ''
        to_remove = open_count  # Number of '(' to remove
        for char in new_str:
            if char == '(' and to_remove > 0:
                to_remove -= 1
            else:
                final_str += char
        
        return final_str