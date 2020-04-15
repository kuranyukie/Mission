# -*- coding: UTF-8 -*-
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# -----------------
# Example:

# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# -----------------

class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]: # 二分法
        orig = {}
        for idx, item in enumerate(nums) :
            if item in orig : orig[item].append(idx)
            else :
                orig[item] = idx
        nums = sorted(nums)
        for i in range(0, len(nums) - 1) :
            if nums[i] + nums[-1] < target : continue
            t2 = target - nums[i]
            a  = i
            b  = len(nums)
            while a + 1 < b :
                m = (a + b) // 2
                if   nums[m] < t2 : a = m
                elif nums[m] > t2 : b = m
                else : 
                    num1 = nums[i]
                    num2 = nums[m]
                    break
        if num1 == num2 :
            return(orig[num1])
        else :
            return([orig[num1], orig[num2]])
    
    def twoSum2(self, nums: List[int], target: int) -> List[int]: # hash搜索
        d = {}
        for idx, item in enumerate(nums) :
            if target - item in d : return [d[target - item], idx]
            d[item] = idx

print(Solution().twoSum1([3,2,4],6))
print(Solution().twoSum2([7,2,7],14))
# print(Solution().twoSum([7,8,9,10,14],18))