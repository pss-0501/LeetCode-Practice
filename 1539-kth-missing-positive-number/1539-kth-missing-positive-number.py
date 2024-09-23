class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1
        res = []
        n = len(arr) + k
        for i in range(n):
            if num not in arr:
                res.append(num)
                num += 1
            else:
                num += 1
        return res.pop(k-1)


