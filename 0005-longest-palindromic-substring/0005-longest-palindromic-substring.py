class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Brute Force
        # n = len(s)
        # longest = ""
        # for i in range(n):
        #     for j in range(i, n):
        #         sub = s[i:j + 1]
        #         if sub == sub[::-1] and len(sub) > len(longest):
        #             longest = sub

        # return longest

        # Optimise
        if len(s) <= 1:
            return s

        def expand(left, right):
            n = len(s)

            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1: right]

        n = len(s)
        long_str = s[0]

        for i in range(n - 1):
            odd_center = expand(i, i)
            even_center = expand(i, i + 1)

            if len(odd_center) > len(long_str):
                long_str = odd_center

            if len(even_center) > len(long_str):
                long_str = even_center


        return long_str
