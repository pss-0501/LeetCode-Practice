class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        word_dict = {}

        for word in words:
            pos = int(word[-1])  
            word_dict[pos] = word[:-1] 
        
        sorted_words = []
         
        for i in sorted(word_dict.keys()):
            sorted_words.append(word_dict[i])
        return " ".join(sorted_words)