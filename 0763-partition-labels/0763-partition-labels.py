class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Greedy -> preprocess

        LastIndex = {}

        for ind, char in enumerate(s):
            LastIndex[char] = ind

        # logic

        res = []
        size, end = 0, 0
        for ind, char in enumerate(s):
            size += 1
            end = max(end, LastIndex[char])
            if ind == end:
                res.append(size)
                size = 0

        return res