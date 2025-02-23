class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat_dict = {}
        s_dict = {}

        word = s.split()
        if len(pattern) != len(word):
            return False

        for i, j in zip(pattern, word):
            pat_dict[i] = j
            s_dict[j] = i

        for i, j in zip(pattern, word):
            if pat_dict[i] != j or s_dict[j] != i:
                return False

        return True

        
