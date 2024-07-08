class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        num = []
        for i in range(1,n + 1):
            num.append(i)


        index = 0  # Start at the 1st friend (index 0)
        while len(num) > 1:
            index = (index + k - 1) % len(num)  # Find the index of the friend to remove
            num.pop(index)
        
        return num[0]
                