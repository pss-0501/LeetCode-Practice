class Solution:
    def binaryGap(self, n: int) -> int:
        bits = bin(n)[2:]
        pos = []
        for i in range(len(bits)):
            if bits[i] == '1':
                pos.append(i)

        if len(pos) < 2:
            return 0

        max_d = 0
        for i in range(1, len(pos)):
            max_d = max(max_d, pos[i] - pos[i - 1])

        return max_d



