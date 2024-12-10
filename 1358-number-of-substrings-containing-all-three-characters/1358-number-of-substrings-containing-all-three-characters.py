class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Brute Force
        # mydict = {}
        # count = 0
        # n = len(s)
        # for i in range(n):
        #     mydict = {0: 0, 1: 0, 2: 0} 
        #     for j in range(i, n):
        #         mydict[ord(s[j]) - ord('a')] = 1
        #         if mydict[0] + mydict[1] + mydict[2] >= 3:
        #             count += (n - j)
        #             break

        # return count 

        # Optimised
        lastseen = {0:-1, 1:-1, 2: -1}
        count = 0
        n = len(s)

        for i in range(n):
            lastseen[ord(s[i]) - ord('a')] = i
            if lastseen[0] != -1 and lastseen[1] != -1 and lastseen[2] != -1:
                count = count + (1 + min(lastseen[0], lastseen[1], lastseen[2]))

        return count
