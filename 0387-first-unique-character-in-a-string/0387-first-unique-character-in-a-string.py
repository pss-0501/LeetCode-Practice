class Solution:
    def firstUniqChar(self, s: str) -> int:
        # BF
        # n = len(s)
        # for i in range(n):
        #     unique = True
        #     for j in range(n):
        #         if i != j and s[i] == s[j]:
        #             unique = False
        #             break
        
        #     if unique:
        #         return i

        # return -1

        # Optimise
        n = len(s)
        my_dict = {}

        for i in s:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1

        for i in range(n):
            if my_dict[s[i]] == 1:
                return i

        return -1