class Solution:
    def maxPower(self, s: str) -> int:
        # if len(s) == 1:

        count = 1
        my_count = 1
        for i in range(1, len(s)):
            if s[i] == s[i -1]:
                count += 1
            else:
                count = 1
            my_count = max(count, my_count)

        return my_count