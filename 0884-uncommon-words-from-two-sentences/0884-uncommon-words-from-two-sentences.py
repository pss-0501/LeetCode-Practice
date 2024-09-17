class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split()
        words2 = s2.split()
        
        # Count occurrences of each word in both sentences
        word_count = Counter(words1 + words2)
        
        # Return words that appear exactly once
        return [word for word, count in word_count.items() if count == 1]
