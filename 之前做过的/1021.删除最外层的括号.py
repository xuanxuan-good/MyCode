#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        # 栈，维护一个只有左括号的栈，当栈不为空才将字符加入到结果中
        res = []
        stack = []
        for c in S:
            if c == "(":
                if stack:
                    res.append(c)
                stack.append(c)
            if c == ")":
                stack.pop()
                if stack:
                    res.append(c)
        return "".join(res)
        
        '''
        # 双指针计数 切片
        i = 0; count = 0
        res = []
        for j in range(len(S)):
            if S[j] == "(":
                count += 1
            if S[j] == ")":
                count -= 1
            if count == 0:
                res.append(S[i+1:j])
                i = j+1
        return "".join(res)
        '''

        '''
        # 单指针计数  针对左括号，上次计数为0（原语的第一个左括号）则不加入；针对右括号（原语的最后一个右括号），上次为1则不加入
        count = 0
        res = []
        for j in S:
            if j == "(" and count > 0:
                res.append(j)
            if j == ")" and count > 1:
                res.append(j)
            count += 1 if j == "(" else -1
        return "".join(res)
        '''
# @lc code=end

