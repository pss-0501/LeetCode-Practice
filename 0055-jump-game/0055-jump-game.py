class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        jmp = 0
        for i in range(n):
            if i > jmp:
                return False
            
            jmp = max(jmp, i + nums[i])


        return True