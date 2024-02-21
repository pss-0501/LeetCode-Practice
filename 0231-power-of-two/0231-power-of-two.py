class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #k = 0
        if n > 0 and (n & (n - 1)) == 0:
            return True