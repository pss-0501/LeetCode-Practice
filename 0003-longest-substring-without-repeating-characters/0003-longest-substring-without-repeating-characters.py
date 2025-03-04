class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mlen = 0
        word = set()
        left = 0

        for right in range(len(s)):
            while s[right] in word:
                word.remove(s[left])
                left += 1
            word.add(s[right])
            mlen = max(mlen, right - left + 1)

        return mlen