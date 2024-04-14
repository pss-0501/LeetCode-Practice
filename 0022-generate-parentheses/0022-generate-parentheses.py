class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backTrack(open1, close1):
            if open1 == close1 == n:
                res.append("".join(stack))
                return
            if open1 < n:
                stack.append('(')
                backTrack(open1 + 1, close1)
                stack.pop()
            
            if close1 < open1:
                stack.append(')')
                backTrack(open1, close1 + 1)
                stack.pop()


        backTrack(0,0)
        return res
