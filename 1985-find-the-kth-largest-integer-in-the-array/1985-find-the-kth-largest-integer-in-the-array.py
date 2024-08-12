class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        int_nums = list(map(int, nums))
        minHeap = int_nums
        heapq.heapify(minHeap)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        return str(minHeap[0])