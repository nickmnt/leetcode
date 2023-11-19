class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key=lambda x: x[0])
        last_end = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < last_end:
                return False
        return True