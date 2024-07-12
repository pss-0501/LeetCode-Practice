class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
    
        for char in s:
            if char == ')':
                # If we encounter a closing parenthesis, we need to reverse the content
                # within the most recent matching parenthesis
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                if stack:
                    stack.pop()  # pop the '('
                # Push the reversed content back onto the stack
                stack.extend(temp)
            else:
                # Otherwise, just push the current character onto the stack
                stack.append(char)
        
        # Join the stack content to form the final result string
        return ''.join(stack)