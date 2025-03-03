class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        num_list = []
        for digit in str(n):
            num_list.append(int(digit))

        for i in range(len(num_list)):
            if i % 2 == 0:
                res += num_list[i]
            else:
                res -= num_list[i]

        return res