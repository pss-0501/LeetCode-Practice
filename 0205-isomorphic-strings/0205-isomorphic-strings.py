class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_to_t_mapping = {}
        t_to_s_mapping = {}

        for s_char, t_char in zip(s, t):
            if s_char in s_to_t_mapping:
                if s_to_t_mapping[s_char] != t_char:
                    return False
            else:
                s_to_t_mapping[s_char] = t_char

            if t_char in t_to_s_mapping:
                if t_to_s_mapping[t_char] != s_char:
                    return False
            else:
                t_to_s_mapping[t_char] = s_char

        return True