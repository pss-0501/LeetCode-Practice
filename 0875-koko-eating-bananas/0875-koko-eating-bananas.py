class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute Force
        def timeToEat(arr, i):
            time = 0
            for a in arr:
                time += math.ceil(a/i)
            return time

        m = max(piles)  
        for i in range(1, m + 1):
            time = timeToEat(piles, i)
            if time <= h:
                return i

        return -1
