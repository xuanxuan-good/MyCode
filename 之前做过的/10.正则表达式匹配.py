#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        '.'用来匹配任意单个字符；'*'用来匹配零个或多个前边那一个元素
        dp[i][j] = true||false 表示s前i个字符 与 p前j个字符是否匹配，下标分别是i-1,j-1
        dp[0][0] = true 两个空串一定是匹配的
        dp[0][j] 表示s是空串，p不是空串 e.g. s = "" p = "a*b*"
            dp[0][1] = false a与""不匹配 [这里字符肯定比s多一个，"*"前边要有字符，"."只能替换字符]
            dp[0][2] = true p[1]='*'可以消除掉a ； dp[0][3] = false b肯定与""不匹配
            dp[0][4] = true
        即dp[0][j] = p[j-1]=="*" and dp[0][j-2]
        状态转移：如果s[i-1]==p[j-1] or p[j-1]=="." 表示对应位置的字符是可以匹配的。
                    那么匹不匹配就要看前边的子串  dp[i][j] = dp[i-1][j-1]
                如果p[j-1]=="*" 分两种情况
                    ① s[i-1] != p[j-2]  e.g. "abc" "abcd*" 不能匹配，要将d用*清除
                        因为只有这一个选择，消除了还有可以匹配的机会--abc abc
                        dp[i][j] = dp[i][j-2]
                    ② s[i-1] == p[j-2] 三种情况  【and j > 1 and p[j-2] != "."】
                        1.s="abc" p="abcc*" 需要消除一个c dp[i][j]=dp[i][j-2]
                        2.s="abc" p="abc*" 需要消除一个*  dp[i][j]=dp[i][j-1]
                        3.s="abc"or"abcc"or"abccc" p="abc*" (子问题即可) dp[i][j]=dp[i-1][j]
        '''
        m, n = len(s), len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(2, n+1):
            dp[0][j] = p[j-1] == "*" and dp[0][j-2]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    if s[i-1] != p[j-2] and j > 1 and p[j-2] != ".":  #?
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-1] or dp[i][j-2] or dp[i-1][j]
        return dp[-1][-1]
        
        '''
        '''
        # 1.递归+记忆化 顺推  相当于是从后向前推，所以返回dp(0, 0)
        # 递归函数dp(i, j)表示s[0..i]和p[0..j]是否匹配，同时用memo存储之前已经处理过的值
        # 如果是已经处理过的，则直接返回存储的值即可；如果p已经匹配完了，s没有匹配完返回false，匹配完返回true
        # pre表示当前p和s的首位是否匹配
        #  判断是否存在‘*’；j < P-2表示是否还剩两个字符以上；P[j+1]=='*'则匹配0次j+2【ab'cd  ab'a*'cd】或者多次i+1【aba'aac  ab'a*c】
        # 如果没有'*'，则直接i+1,j+1
        # 更新memo[(i, j)] = tmp
        '''
        m, n = len(s), len(p)
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == n:
                return i == m
            pre = i < m and p[j] in {s[i], "."}
            if j <= n-2 and p[j+1] == '*':  # j <= 
                tmp = dp(i, j+2) or pre and dp(i+1, j)
            else:
                tmp = pre and dp(i+1, j+1)
            memo[(i, j)] = tmp
            return tmp
        return dp(0, 0)
        '''

        '''
        '''
        # 有重复
        # 如果p为空，则s也为空返回true（即not s）;s不空则false
        # s有值并且p[0]=s[0]|'.' -- first：表示s和p的第一位是否匹配成功
        # 如果p的长度大于等于2，并且p[1]='*'--则可以匹配0次s[1:]+first或多次p[2:]
        # 反之没有*，s[1:],p[1:]直接向后匹配即可
        '''
        if not p:
             return not s
        first = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or first and self.isMatch(s[1:], p)
        else:
            return first and self.isMatch(s[1:], p[1:])
        '''
# @lc code=end

