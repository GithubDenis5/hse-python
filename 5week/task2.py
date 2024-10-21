"""
leetcode.com/problem-list/hash-table/
https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=problem-list-v2&envId=string
"""


class Solution(object):
    def letterCombinations(self, digits):
        dictNum = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        a = []
        if digits:
            for i in dictNum[int(digits[0])]:
                a.append(i)
            for _ in range(1, len(digits)):
                for i in range(len(a)):
                    c = a.pop(0)
                    for j in dictNum[int(digits[_])]:
                        a.append(c + j)

        return a
