class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < (m * k):
            return -1
        
        def canMakeBouquets(day):
            flower = 0
            Bouquets = 0

            for b in bloomDay:
                if b <= day:
                    flower += 1
                    if flower == k:
                        Bouquets += 1
                        flower = 0
                else:
                    flower = 0
            if Bouquets >= m:
                    return True  # We can make the required number of bouquets
            return False

        # Step 2: Binary search on result
        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if canMakeBouquets(left) else -1