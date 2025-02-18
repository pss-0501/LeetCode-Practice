class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Brute Force
        # if not strs:
        #     return ""

        # lcp = strs[0]

        # for i in range(len(lcp)):
        #     for j in strs:
        #         if i >= len(j) or j[i] != lcp[i]:
        #             return lcp[:i]

        # return lcp

        # Optimised
        sort_array = sorted(strs)
        first = sort_array[0]
        last = sort_array[-1]

        res = []

        for i in range(len(first)):
            if first[i] != last[i]:
                break
            res.append(first[i])

        return "".join(res)