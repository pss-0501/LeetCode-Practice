class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count frequency of each letter in the word
        freq = Counter(word)
        
        # Sort the frequencies in descending order
        sorted_freq = sorted(freq.values(), reverse=True)

        res = 0
        for i in range(len(sorted_freq)):
            res += ceil((i + 1 )/ 8) * sorted_freq[i]
        return res

