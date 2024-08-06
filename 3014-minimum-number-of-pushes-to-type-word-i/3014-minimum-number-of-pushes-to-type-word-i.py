class Solution:
    def minimumPushes(self, word: str) -> int:
        res = 0
        for i in range(1, len(word) + 1):
            res += ceil(i/8)
        return res