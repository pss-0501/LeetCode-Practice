class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combs = []

        def helper(i, curComb):
            if sum(curComb) == target:
                combs.append(curComb.copy())
                return

            if sum(curComb) > target:
                return
            
            if i >= len(candidates):
                return

            # Include candidates[i]
            curComb.append(candidates[i])
            helper(i + 1, curComb)  # Include the same element again

            # Backtrack
            curComb.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            helper(i + 1, curComb)  # Move to the next element
        
        helper(0, [])
        return combs