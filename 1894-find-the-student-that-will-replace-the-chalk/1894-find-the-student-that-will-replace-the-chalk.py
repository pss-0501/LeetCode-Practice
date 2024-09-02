class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        #Brute Force
        # index = 0
        # while k > 0:
        #     if index > len(chalk) - 1:
        #         index = 0
        #     k = k - chalk[index]
        #     if k < 0:
        #         return index
        #     index += 1

        # return 0

        total_chalk = sum(chalk)
        k = k % total_chalk  # Reduce k to a smaller equivalent value

        for i, chalk_needed in enumerate(chalk):
            if k < chalk_needed:
                return i
            k -= chalk_needed

        return -1
