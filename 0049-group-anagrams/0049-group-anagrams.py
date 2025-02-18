class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        my_dict = {}
        for s in strs:
            string = ''.join(sorted(s))
            if string in my_dict:
                my_dict[string].append(s)
            else:
                my_dict[string] = [s]
        return list(my_dict.values())
