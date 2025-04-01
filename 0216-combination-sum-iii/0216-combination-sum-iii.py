class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        res = []

        def dfs(i, curr, total):
            if total == n and len(curr) == k:
                res.append(curr.copy())
                return

            if i >= len(nums) or total > n or len(curr) > k:
                return

            curr.append(nums[i])
            dfs(i + 1, curr, total + nums[i])

            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res
            
