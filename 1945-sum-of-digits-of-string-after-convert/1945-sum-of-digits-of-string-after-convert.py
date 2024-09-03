class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ""
        for char in s:
            num_str += str(ord(char) - ord('a') + 1)

        for _ in range(k):
            total = 0
            for digit in num_str:
                total += int(digit)
            num_str = str(total)
    
        return int(num_str)
