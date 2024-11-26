class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxLength = 0
        res = set()

        for end in range(len(s)):
            while s[end] in res:
                res.remove(s[start])
                start += 1

            res.add(s[end])
            maxLength = max(maxLength, end - start + 1)

        return maxLength


            