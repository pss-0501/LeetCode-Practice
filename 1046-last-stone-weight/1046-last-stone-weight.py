class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ## Brute Force
        # stones.sort()
        # while len(stones) > 1:
        #     y = stones.pop()
        #     x = stones.pop()
        #     if y == x:
        #         stones.append(0)
        #         stones.sort()
        #     if x != y and x < y:
        #         a = y - x
        #         stones.append(a)
        #         stones.sort()
            
        # return stones[0]

        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)
            if y == x:
                heapq.heappush(maxHeap, 0)

            if y != x and x<y:
                a = y-x
                heapq.heappush(maxHeap, -a)

        return -maxHeap[0]

