class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        per = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1

        def backtrack():
            if len(per) == len(nums):
                ans.append(per.copy())
                return

            for i in count:
                if count[i] > 0:
                    per.append(i)
                    count[i] -= 1

                    backtrack()

                    count[i] += 1
                    per.pop()

        backtrack()
        return ans