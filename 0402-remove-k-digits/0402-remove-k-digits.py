class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i in num:
            while k > 0 and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)

        stack = stack[:len(stack) - k]
        while stack and stack[0] == '0':
            stack.pop(0)
        return "".join(stack) if stack else "0"