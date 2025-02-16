class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_dict = {}
        for i in s:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1

        for i in t:
            if i not in my_dict:
                return False
            elif i in my_dict:
                my_dict[i] -= 1
                if my_dict[i] == 0:
                    del my_dict[i]

        return True