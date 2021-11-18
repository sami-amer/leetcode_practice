from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        hold_start = None
        hold_end = None
        res = []
        for i in range(len(intervals)):
            if i == len(intervals) - 1:
                if (hold_start and hold_end) or (hold_start == 0):
                    res.append([hold_start,hold_end])
                else:
                    res.append(intervals[i])
                return res

            curr_interval = intervals[i]
            next_interval = intervals[i + 1]
            if (hold_start and hold_end) or (hold_start == 0):
                if next_interval[0] <= hold_end:
                    if next_interval[1] > hold_end:
                        hold_end = next_interval[1]
                    continue
                else:
                    res.append([hold_start,hold_end])
                    hold_end, hold_start = None, None
                    continue

            if curr_interval[1] >= next_interval[0]:
                hold_start = curr_interval[0]
                hold_end = max(curr_interval[1], next_interval[1])
            else:
                res.append(intervals[i])
        return res



if __name__ == '__main__':
    # intervals = [[1,3],[2,6],[8,10],[15,18]]
    # output = [[1,6],[8,10],[15,18]]
    # intervals = [[1,4],[0,4]]
    # intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    intervals = [[1,4],[0,2],[3,5]]
    print(Solution.merge(None,intervals))