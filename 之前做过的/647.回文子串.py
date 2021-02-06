#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        # 1.dp [n][n] 表示i到j的子串是否是回文串  针对首尾
        n = len(s)
        res = 0
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1):  # 逆序 对每个n-1->i
            for j in range(i, n):  # 正序 每个i->n
                dp[i][j] = s[i] == s[j] and((j-i+1) < 3 or dp[i+1][j-1])  # 前后字符相同，内部只有1,2个字符 或者 子串内的子串 是否是回文
                res += dp[i][j]  # 0+true = 1
        return res
        
        '''
        # 4. Manacher 算法:在所有字符中间插入一个没有出现过的字符，则变成只有奇数的情况；于是可以每一个字符作为中心点判断回文（会利用已经计算出来的状态）
        # 2.中心扩展法，一个或者两个中心
        n = len(s)
        res = 0
        for center in range(2 * n - 1):  # 范围
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
            # 如果要求最长回文串。可以maxres = max(maxres, (right-left+1))
                res += 1
                left -= 1
                right += 1
        return res
        '''
        
        '''
        return sum(s[i:j] == s[i:j][::-1] for j in range(len(s)+1) for i in range(j))
        '''
# @lc code=end

