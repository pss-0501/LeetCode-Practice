class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []

        def helper(i, curCombs, combs, n, k):
            if len(curCombs) == k:
                combs.append(curCombs.copy())
                return

            if i > n:
                return
            
            # include i
            curCombs.append(i)
            helper(i+1, curCombs, combs, n, k)
            curCombs.pop()

            # not include i
            helper(i+1, curCombs, combs, n, k)


        helper(1, [], combs, n, k)
        return combs