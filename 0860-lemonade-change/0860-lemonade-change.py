class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # change = []
        # for i in bills:
        #     if i == 5:
        #         change.append(5)
        #         continue
        #     if i == 10 and change.count(5) >= 1:
        #         change.remove(5)
        #         change.append(10)
        #         continue
        #     if i == 20 and change.count(5) >= 1 and (change.count(5) >= 3 or change.count(10) >= 1):
        #         if change.count(10) >= 1: 
        #             change.remove(10)
        #             change.remove(5)
        #         else:
        #             change.remove(5)
        #             change.remove(5)
        #             change.remove(5)
        #         change.append(20)
        #         continue
        #     else:
        #         return False

        # return True

        five = 0
        ten = 0
        for n in bills:
            if n == 5:
                five += 1
                continue
            if n == 10 and five >= 1:
                five -= 1
                ten += 1
                continue
            if n == 20:
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                    continue
                elif five >= 3:
                    five -= 3
                    continue
                else:
                    return False
            else:
                return False
        return True