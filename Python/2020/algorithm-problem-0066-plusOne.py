# -*- coding: UTF-8 -*-
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]: # 32 ms  13.7 MB
        if digits[-1] != 9 :
            return digits[:-1] + [digits[-1]+1]
        else :
            i = -1
            while digits[i] == 9 :
                digits[i] = 0
                if i == - len(digits) :
                    return [1] + digits
                i -= 1
            digits[i] += 1
            return digits