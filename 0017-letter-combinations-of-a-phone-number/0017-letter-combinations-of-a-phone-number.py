class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        ans, sol = [], []
        
        # Mapping of digits to letters
        letter_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtracking(i = 0):
            # base case
            if i == len(digits):
                ans.append("".join(sol))
                return

            key_pressed = letter_dict[digits[i]]

            for letter in key_pressed:
                sol.append(letter)
                backtracking(i + 1)
                sol.pop()

        backtracking(0)
        return ans