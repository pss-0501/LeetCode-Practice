class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = []
        for i in bills:
            if i == 5:
                change.append(5)
                continue
            if i == 10 and change.count(5) >= 1:
                change.remove(5)
                change.append(10)
                continue
            if i == 20 and change.count(5) >= 1 and (change.count(5) >= 3 or change.count(10) >= 1):
                if change.count(10) >= 1: 
                    change.remove(10)
                change.remove(5)
                change.append(20)
                continue
            else:
                return False

        return True