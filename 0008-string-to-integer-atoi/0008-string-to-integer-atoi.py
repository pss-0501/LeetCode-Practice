class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        s = s.lstrip()

        if not s:
            return 0

        i = 0
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            i += 1
            sign = -1

        result = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break
            i += 1

        result *= sign

        result = max(INT_MIN, min(result, INT_MAX))

        return result
