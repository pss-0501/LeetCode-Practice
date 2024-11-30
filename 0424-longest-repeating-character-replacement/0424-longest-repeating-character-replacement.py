class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        n = len(s)
        flip = 0
        mydict = {}     # char, value
        # changes == len - maxfreq
        maxLen = 0
        maxFreq = 0

        for right in range(n):
            mydict[s[right]] = mydict.get(s[right], 0) + 1
            maxFreq = max(maxFreq, mydict[s[right]])

            while (right - left + 1) - maxFreq > k:
                mydict[s[left]] -= 1
                if mydict[s[left]] == 0:
                    del mydict[s[left]]
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen

            




