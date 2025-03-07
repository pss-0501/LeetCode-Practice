class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start < res[-1][1] or end < res[-1][0]:
                return False
            res.append([start, end])
        return True