"""
leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/repeated-dna-sequences/submissions/1456061814/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        sequence_l = 10
        seen = set()
        rep = set()

        for i in range(len(s) - sequence_l + 1):
            sub = s[i : i + sequence_l]
            if sub in seen:
                rep.add(sub)
            else:
                seen.add(sub)

        return list(rep)
