# -*- coding: UTF-8 -*-
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first, second  = -1, -1
        for idx, item in enumerate(nums) :
            if item == first : second = item
            elif item > first : 
                second = first
                first, first_idx = item, idx
            elif item < first and item >= second : second = item
        if first >= second * 2 : return first_idx
        else : return -1