# -*- coding: UTF-8 -*-
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/interval-list-intersections/

from typing import *

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]: #172 ms  14.5 MB
        output = []
        i, j = 0, 0
        while i < len(A) and j < len(B) :
            a_in, a_out, b_in, b_out = A[i], B[j]

            if   a_out < b_in : i += 1   # 不相交 A在左侧，挪A
            elif b_out < a_in : j += 1   # 不相交 B在左侧，挪B

            elif a_in <= b_in <= b_out <= a_out : output.append([b_in, b_out]); j += 1 # A包住B，挪B
            elif b_in <= a_in <= a_out <= b_out : output.append([a_in, a_out]); i += 1 # B包住A，挪A

            elif a_in <= b_in <= a_out <= b_out : output.append([b_in, a_out]); i += 1 # 相交情况，A在左边，挪A
            elif b_in <= a_in <= b_out <= a_out : output.append([a_in, b_out]); j += 1 # 相交情况，B在左边，挪B
        return output