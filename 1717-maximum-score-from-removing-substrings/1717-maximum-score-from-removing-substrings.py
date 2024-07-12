class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(s, a, b, points):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] == a and char == b:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return "".join(stack), score

        if x > y:
            # Prioritize removing "ab" first
            s, score1 = remove(s, 'a', 'b', x)
            s, score2 = remove(s, 'b', 'a', y)
        else:
            # Prioritize removing "ba" first
            s, score1 = remove(s, 'b', 'a', y)
            s, score2 = remove(s, 'a', 'b', x)
        
        return score1 + score2