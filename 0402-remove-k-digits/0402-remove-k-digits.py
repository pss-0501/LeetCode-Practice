class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # n = len(num)
        stack = []
        for i in num:

            while stack and stack[-1] > i and k > 0:
                stack.pop()
                k -= 1


            stack.append(i)

        # stack = stack[:-k] if k > 0 else stack
        while k > 0:
            stack.pop()
            k -= 1

        res = ''.join(stack).lstrip('0')

        return res if res else "0"