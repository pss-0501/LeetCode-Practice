class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """


        counter = 0
        for i in words:
            for letter in i:
                if letter not in allowed:
                    counter += 1
                    break
        return len(words) - counter
        