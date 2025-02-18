class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for i in strs:
            sorted_words = ''.join(sorted(i))      #make this key for same words
            anagram_dict[sorted_words].append(i)

        return list(anagram_dict.values())