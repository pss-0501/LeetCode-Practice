class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in s:
            if stack and ((i == 'B' and stack[-1] == 'A') or (i == 'D' and stack[-1] == 'C')) :
                stack.pop()
                continue
            print(stack)
            
            stack.append(i)

        return len(stack)