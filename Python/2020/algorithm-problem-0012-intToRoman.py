# -*- coding: UTF-8 -*-
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        list1 = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        list2 = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        result= ""
        for i in range(len(list1)):
            while num >= list1[i]:
                result += list2[i]
                num    -= list1[i]
        return result
    
    def intToRoman2(self, num: int) -> str:
        st = f'{num:04}'
        unpacked = [int(st[0])*1000, int(st[1])*100, int(st[2])*10, int(st[3])]
        print(unpacked)
        output = ''
        mapping = {
            1000: 'M',
            2000: 'MM', 
            3000: 'MMM',
            100 : 'C',
            200 : 'CC', 
            300 : 'CCC', 
            400 : 'CD',
            500 : 'D',
            600 : 'DC',
            700 : 'DCC',
            800 : 'DCCC',
            900 : 'CM',
            10  : 'X',
            20  : 'XX',
            30  : 'XXX',
            40  : 'XL',
            50  : 'L',
            60  : 'LX',
            70  : 'LXX',
            80  : 'LXXX',
            90  : 'XC',
            1   : 'I',
            2   : 'II',
            3   : 'III',
            4   : 'IV',
            5   : 'V',
            6   : 'VI',
            7   : 'VII',
            8   : 'VIII',
            9   : 'IX',
            0   : ''
        }
        for n in unpacked:
            print(n)
            output += mapping[n]
        return output

