# -*- coding: UTF-8 -*-
# 链接：https://leetcode-cn.com/problems/find-pivot-index

class Solution:
    def pivotIndex1(self, nums: List[int]) -> int: # 暴力左右相等 时间太长
        for i in range(0, len(nums)) :
            left  = nums[:i]
            right = nums[i+1:]
            if sum(left) == sum(right) :
                return i
        return -1

    def pivotIndex2(self, nums: List[int]) -> int: # while循环 312 ms 14.7 MB
        if len(nums) == 0: return -1
        right = sum(nums) - nums[0]
        left  = 0
        idx   = 0
        while idx < len(nums):
            if left == right : return idx
            left += nums[idx]
            right -= nums[idx + 1] if idx + 1 < len(nums) else 0
            idx += 1
        return -1

    def pivotIndex3(self, nums: List[int]) -> int: # for循环 188 ms 14.8 MB
        if len(nums) == 0: return -1
        s = sum(nums)
        left  = 0
        for idx, item in enumerate(nums) :
            if left == s - item - left : return idx
            left += item
        return -1