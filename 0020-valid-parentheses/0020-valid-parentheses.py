class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # A dictionary to match closing and opening brackets
        matching = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in matching.values():  # If it's an opening bracket
                stack.append(char)
            elif char in matching:  # If it's a closing bracket
                # Check if the stack is empty or top of stack doesn't match
                if not stack or stack.pop() != matching[char]:
                    return False
            else:
                return False

        return not stack