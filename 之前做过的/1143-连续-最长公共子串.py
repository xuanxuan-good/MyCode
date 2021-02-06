# 字符串最长子串  "abbcc" "abcc" --- ab 2; bcc 3 --最长的是3
# 子串，是找连续的；；而子序列可以是不连续的

# 暴力, 依次遍历最短的子串还是最长的子串，循环是怎么循环的

# 递归+记忆化，自顶向下
    # if len(text1) == 0 or len(text2) == 0: return 0
    # if text1[0] == text2[0]: return self.method(text1[1:], text2[1:]) + 1
    # else return self.method(tex1[1:], text2[1:])

# 动态规划：自底向上 O(mn) O(mn) dp[m+1][n+1] dp[i][j]表示text1[:i+1]和text2[:j+1]的最长子串
    # 初始化 0行 0列 都是0
    # 状态方程 dp[i][j] = dp[i-1][j-1] + 1 if text1[i-1] == text2[j-1] else 
            # dp[i][j] = 0  [因为必须是连续的，如果有不等的，就为0了，重新开始找]