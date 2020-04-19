# -*- coding: UTF-8 -*-
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-intervals/

from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: # 36 ms 14.5 MB
        if len(intervals) == 0: return intervals
        intervals.sort(key=lambda x: x[0])
        output = []
        temp_small, temp_large = intervals[0]
        for idx in range(len(intervals)):
            if intervals[idx][0] <= temp_large:
                if intervals[idx][1] > temp_large : temp_large = intervals[idx][1]
            else:
                output.append([temp_small, temp_large])
                temp_small, temp_large = intervals[idx]
        output.append([temp_small, temp_large])
        return output

print(Solution().merge([[1,3], [2,6], [2,4], [7,9], [11,236], [236,240]]))