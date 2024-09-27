"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/integer-to-roman/submissions/1404047394/?envType=problem-list-v2&envId=string&difficulty=MEDIUM
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""

        # div 1000 != 0
        if num // 1000 != 0:
            result += ('M' * (num // 1000))

        # div 100 mod 10 != 0
        if num // 100 % 10 != 0:
            match num // 100 % 10:
                case 1:
                    result += "C"
                case 2:
                    result += "CC"
                case 3:
                    result += "CCC"
                case 4:
                    result += "CD"
                case 5:
                    result += "D"
                case 6:
                    result += "DC"
                case 7:
                    result += "DCC"
                case 8:
                    result += "DCCC"
                case 9:
                    result += "CM"

        if num // 10 % 10 != 0:
            match num // 10 % 10:
                case 1:
                    result += "X"
                case 2:
                    result += "XX"
                case 3:
                    result += "XXX"
                case 4:
                    result += "XL"
                case 5:
                    result += "L"
                case 6:
                    result += "LX"
                case 7:
                    result += "LXX"
                case 8:
                    result += "LXXX"
                case 9:
                    result += "XC"

        if num % 10 != 0:
            match num % 10:
                case 1:
                    result += "I"
                case 2:
                    result += "II"
                case 3:
                    result += "III"
                case 4:
                    result += "IV"
                case 5:
                    result += "V"
                case 6:
                    result += "VI"
                case 7:
                    result += "VII"
                case 8:
                    result += "VIII"
                case 9:
                    result += "IX"

        return result
