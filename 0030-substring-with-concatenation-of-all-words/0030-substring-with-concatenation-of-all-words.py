class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        total_word_length = word_length * len(words)
        words_count = Counter(words)
        start_indexes = []

        for i in range(len(s) - total_word_length + 1):
            substring = s[i:i + total_word_length]

            # Split the substring into chunks of `word_length`
            seen_words = [substring[j:j + word_length] for j in range(0, total_word_length, word_length)]
                    
            if Counter(seen_words) == words_count:
                start_indexes.append(i)

        return start_indexes