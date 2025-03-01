class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_i = []
        stack_j = []
        for i in s:
            if i == '#':
                if stack_i:
                    stack_i.pop()
            else:
                stack_i.append(i)

        for j in t:
            if j == '#':
                if stack_j:
                    stack_j.pop()
            else:             
                stack_j.append(j)

        return stack_i == stack_j