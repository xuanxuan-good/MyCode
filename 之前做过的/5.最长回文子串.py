#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 要找最长，肯定是有最优子结构的
        '''
        # 1.暴力【枚举起点和终点】 O(n^3) 列举出所有的子串，判断是否是回文，保存最长的  94/176 time limit
        # sdfghj
        # .   .
        #  .   .
        def isPalindrome(s):
            left, right = 0, len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        # 特判
        if len(s) < 2:
            return s
        ans = s[0]
        maxs = 1
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if isPalindrome(s[i:j+1]) and (j-i+1) > maxs:
                    maxs = j-i+1
                    ans = s[i:j+1]
        return ans
        '''

        '''
        # √ 2.中心扩散【枚举中心】，O(n^2) O(1) 遍历每一个字符，以此为中心，找能到达的最长的回文子串
        size = len(s)
        if size < 2:
            return s
        self.maxs = 1
        self.lo = 0
        for i in range(len(s)):
            self.center_spread(s, size, i, i)
            self.center_spread(s, size, i, i+1)
        return s[self.lo:self.lo+self.maxs]

    def center_spread(self, s, size, left, right):
        '''
        # left = right 时，回文中心是一个字符，回文串长度是奇数
        # left = right+1 时，回文中心是一个字符，回文串长度是偶数
        # 向两边扩散
        '''
        i, j = left, right
        while i >= 0 and j < size and s[i] == s[j]:  # i >= 0 有等号
            i -= 1
            j += 1
        if self.maxs < j - i - 1:  # j - i + 1 -2  因为最后不满足之前多向外扩展了两个字符
            self.maxs = j - i - 1
            self.lo = i + 1
        '''

        # 3.动态规划  O(n^2) O(n^2) [原字符串的一个子串是否为回文]
        # 如果一个字符串的头尾两个字符都不相等，那么一定不是回文；相等才可以据需判断
        # 定义状态 dp[i][j] 表示子串s[i..j]是否为回文；因为要构成子串，因此i<=j，只需要表格对角线以上的部分
        # 状态转移方程  dp[i][j] = (s[i]==s[j]) and dp[i+1][j-1]
                    # 边界条件[i+1, j-1]不构成区间，即长度严格小于2 -- (j-1)-(i+1)+1 < 2 即j-i<3 [也就是j-i+1<4,针对长度等于2或3的子串，只需要判断头尾是否相等即可]
                        # [i+1, j-1]只有一个字符，显然是回文；为空串则[i,j]一定回文
                # 初始化 单个字符一定是回文 dp[i][i]=true
                # 只要dp[i][j]=true,记录子串长度和起始位置即可，截取会消耗性能   1~size-1; 0~j-1
        size = len(s)
        if size < 2:
            return s
        max_len, start = 1, 0
        dp = [[False] * size for _ in range(size)]
        for i in range(size):
            dp[i][i] = True
        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:  # 前提
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]

        # 4.Manacher算法，在中心扩散的基础上，不需要考虑子串中字符偶数个数的情况，全部变成奇数个字符
# @lc code=end

