class Solution:
    def reverseWords(self, s: str) -> str:

        word = s.split()
        res = []
        for i in range(len(word) - 1, -1, -1):
            res.append(word[i])
            res.append(' ')

        return "".join(res).strip()

            