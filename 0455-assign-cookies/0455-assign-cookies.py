class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g_sort = sorted(g)
        s_sort = sorted(s)

        left, right = 0, 0
        res = 0
        while right < len(s) and left < len(g):
            if g_sort[left] <= s_sort[right]:
                res += 1
                left += 1
            right += 1

        return res
            
