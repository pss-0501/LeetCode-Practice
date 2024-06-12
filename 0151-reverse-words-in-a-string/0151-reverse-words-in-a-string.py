class Solution:
    def reverseWords(self, s: str) -> str:
        terms_list = s.split()
        result_string = ""
        for i in range(len(terms_list) - 1,-1,-1):
            result_string = result_string + " " + terms_list[i]
            # if i != 0:
            #     result_string 

        return result_string.strip()