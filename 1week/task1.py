"""
leetcode.com/problem-list/string/
url:https://leetcode.com/problems/string-to-integer-atoi/?envType=problem-list-v2&envId=string&favoriteSlug=&difficulty=MEDIUM
"""

class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0

        num = 0
        flag_sing = 1
        i = 0
        max_int = 2**31-1
        min_int = -2**31

        if s[i] == '-':
            flag_sing *= -1
            i += 1
        elif s[i] == '+':
            i += 1
        

        while i < len(s) and s[i].isdigit():
            num = num *10 + int(s[i])
            i += 1
            if flag_sing * num > max_int:
                return max_int
            if flag_sing* num < min_int:
                return min_int
            
        return flag_sing *num

    

