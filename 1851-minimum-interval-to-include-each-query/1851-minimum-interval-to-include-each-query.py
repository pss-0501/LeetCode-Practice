class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        # Sort queries and store original index for final output
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])

        min_heap = []  # Min-heap to store valid intervals (size, right)
        result = [-1] * len(queries)  # Final output
        i = 0  # Pointer for intervals

        for query_index, query in sorted_queries:
            # Add all intervals that start before or at the query
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                heapq.heappush(min_heap, (right - left + 1, right))  # (size, right)
                i += 1

            # Remove intervals that end before the query
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            # If heap is not empty, get the smallest interval size
            if min_heap:
                result[query_index] = min_heap[0][0]

        return result