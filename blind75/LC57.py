from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort()
        
        res = []
        
        last = intervals[0]
        
        for interval in intervals:
            if interval[0] <= last[1]:
                last[1] = max(interval[1], last[1])
            else:
                res.append(last)
                last = interval
        res.append(last)

if __name__ == '__main__':
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    # output = [[1,5],[6,9]]
    print(Solution.insert(None,intervals, newInterval))
