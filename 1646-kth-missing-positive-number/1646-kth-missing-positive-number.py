class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Brute Force
        # num = 1
        res = []
        n = len(arr) + k
        for i in range(1,n + 1):
            if i not in arr:
                res.append(i)
                # num += 1
            # else:
            #     num += 1
        return res.pop(k-1)

        # Optimise


