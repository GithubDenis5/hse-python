"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/compare-version-numbers/?envType=problem-list-v2&envId=string&difficulty=MEDIUM
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        list_v1 = version1.split('.')
        list_v2 = version2.split('.')

        max_len = max(len(list_v1), len(list_v2))

        for i in range(max_len):
            v1 = 0
            v2 = 0
            
            if i < len(list_v1):
                v1 = int(list_v1[i])
            if i < len(list_v2):
                v2 = int(list_v2[i])
            
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
            
        return 0
