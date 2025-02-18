class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        lcp = strs[0]

        for i in range(len(lcp)):
            for j in strs:
                if i >= len(j) or j[i] != lcp[i]:
                    return lcp[:i]

        return lcp


