class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_dict = {}

        for i in range(len(s)):
            if s[i] not in my_dict.keys():
                my_dict[s[i]] = t[i]
            else:
                if my_dict[s[i]] != t[i]:
                    return False

        my_dict = {}
        for i in range(len(t)):
            if t[i] not in my_dict.keys():
                my_dict[t[i]] = s[i]
            else:
                if my_dict[t[i]] != s[i]:
                    return False

        return True