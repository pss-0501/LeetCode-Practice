class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in s:
            if i.isalpha():
                stack.append(i)
            print(stack)
            if i.isdigit() and stack:
                stack.pop()

        return "".join(stack)