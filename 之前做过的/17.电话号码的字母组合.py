#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # bfs
        if not digits:
            return []
        result = [""]
        m = {'2': "abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        for digit in digits:
            newresult = []
            for char in m[digit]:
                for strs in result:
                    newresult.append(strs+char)
            result = newresult
        return result
        '''
        # dfs
        if not digits:
            return []
        ret = []
        m = {'2': "abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        def dfs(m, digits, path, ret):
            # terminator
            if not digits:
                ret.append(path)
                return
            # current logic ; drill down
            for c in m[digits[0]]:
                dfs(m, digits[1:], path+c, ret)
            # reverse
        dfs(m, digits, "", ret)
        return ret
        '''
# @lc code=end

