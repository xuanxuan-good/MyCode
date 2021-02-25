#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
'''
# 思路：因为有最长字眼，所以考虑用dp来做
    用dp[i]表示 从开始到第i个下标结尾的字符 组成的最长合法括号序列长度
    需要根据i位置处字符是什么进行判断。
    1. s[i] = '(' i处字符不能和前边的i-1处字符进行匹配。dp[i] = 0
    2. s[i] = ')' 此时有可能与前边的字符匹配，需要根据s[i - 1]是什么进行判断
       [1] s[i - 1] = '(' 此时下标i与i-1处的字符是能匹配上的; i-1 处是'(',dp[i - 1] = 0; dp[i - 2]是之前的最长长度，dp[i] = dp[i - 2] + 2
       [2] s[i - 1] = ')' 下标i与i-1处的字符不匹配，((A))情况下有匹配的可能；否则dp[i] = 0.
            要找到与s[i]对应的位置：i - dp[i - 1] - 1, s[i - dp[i - 1] - 1]是‘(’，则是一对合法的括号：d[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                                                                                                                这里相当于是AB形式，还需要把A处有效括号的长度加上
其中[1][2]可以合并
这里多了两种括号，[],{}, 判断条件都是相同的，加上相应判断即可
'''

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        for i in range(n):
            if s[i] == ')' and i-1-dp[i-1] >= 0 and s[i-1-dp[i-1]] == '(':
                dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
        return max(dp)
# @lc code=end



# # 只有（）代码
# def VaildSequence(s):
#     n = len(s)
#     if n == 0:
#         return 0
#     res = 0
#     dp = [0] * n
#     for i in range(1, n):
#         if s[i] == ')':
#             if s[i - 1] == '(':
#                 dp[i] = 2
#                 if i - 2 >= 0:
#                     dp[i] += dp[i - 2]
#             elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
#                 dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
#     return max(dp)

# s = '({({(({()}})}{())})})[){{{([)()((()]]}])[{)]}{[}{)'  # 4
# # s = ''  # 0
# # s = '()'  # 2
# res = VaildSequence(s)
# print(res)



# 三种括号都有代码
def VaildSequence(s):
    n = len(s)
    if n == 0:
        return 0
    res = 0
    dp = [0] * n
    for i in range(1, n):
        if (s[i] == ')' and s[i - 1] == '(') or (s[i] == ']' and s[i - 1] == '[') or (s[i] == '}' and s[i - 1] == '{'):
            dp[i] = 2
            if i - 2 >= 0:
                dp[i] += dp[i - 2]
        elif (s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(') or (s[i] == ']' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '[') or (s[i] == '}' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '{'):
                dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
    return max(dp)

# s = '({({(({()}})}{())})})[){{{([)()((()]]}])[{)]}{[}{)'  # 4
# s = ''  # 0
# s = '()'  # 2
s = '()()([(]))'  # 4
res = VaildSequence(s)
print(res)