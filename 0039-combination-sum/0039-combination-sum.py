class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
            helper(i, curComb)  # Include the same element again

            # Backtrack
            curComb.pop()
            helper(i + 1, curComb)  # Move to the next element
        
        helper(0, [])
        return combs