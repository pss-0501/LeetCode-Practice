class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            if y == x:
                x = y = 0
            if x != y and x < y:
                a = y - x
                stones.append(a)
                stones.sort()
            
        return stones[0]
