class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count=0
        max_end=0
        for i in intervals:
            if i[1]>max_end:
                count+=1
                max_end=i[1]
        return count