"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/simplify-path/submissions/1404107219/?envType=problem-list-v2&envId=string&difficulty=MEDIUM
"""


class Solution:
    def simplifyPath(self, path: str) -> str:

        path_list = []
        i_of_path_list = -1
        path += '/'
        for i in range(1, len(path)):
            if i != 0 and path[i] != "/" and path[i - 1] == "/":
                i_of_path_list += 1
                path_list.append(path[i])
            elif path[i] != "/":
                path_list[i_of_path_list] += path[i]
            elif path[i] == "/" and path[i - 1] != "/":
                match path_list[i_of_path_list]:
                    case ".":
                        if len(path_list) != 0:
                            path_list.pop()
                            i_of_path_list -= 1
                    case "..":
                        if len(path_list) != 0:
                            path_list.pop()
                            if len(path_list) > 0:
                                path_list.pop()
                                i_of_path_list -= 1
                            i_of_path_list -= 1

        result = "/"
        for dir in path_list:
            result += dir + "/"

        if len(result) > 1:
            result = result[:-1]

        return result
