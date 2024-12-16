class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        left = 0
        curr_sum = 0

        # if k == 0:
        #     return res

        for right in range(n + abs(k)):
            curr_sum += code[right % n]

            if right - left + 1 > abs(k):
                curr_sum -= code[left % n]
                left = (left + 1) % n

            if right - left + 1 == abs(k):
                if k > 0:
                    res[(left - 1) % n] = curr_sum 

                elif k < 0:
                    res[(right + 1) % n] = curr_sum

        return res