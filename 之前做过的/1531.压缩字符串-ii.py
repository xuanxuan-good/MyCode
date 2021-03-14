#
# @lc app=leetcode.cn id=1531 lang=python3
#
# [1531] 压缩字符串 II
# 行程长度编码 是一种常用的字符串压缩方法，它将连续的相同字符（重复 2 次或更多次）替换为字符和表示字符计数的数字（行程长度）。
# 例如，用此方法压缩字符串 "aabccc" ，将 "aa" 替换为 "a2" ，"ccc" 替换为` "c3" 。因此压缩后的字符串变为 "a2bc3" 。
# 注意，本问题中，压缩时没有在单个字符后附加计数 '1' 。
# 给你一个字符串 s 和一个整数 k 。你需要从字符串 s 中删除最多 k 个字符，以使 s 的行程长度编码长度最小。
# 请你返回删除最多 k 个字符后，s 行程长度编码的最小长度 。

# 示例 1：
# 输入：s = "aaabcccd", k = 2
# 输出：4
# 解释：在不删除任何内容的情况下，压缩后的字符串是 "a3bc3d" ，长度为 6 。最优的方案是删除 'b' 和 'd'，这样一来，压缩后的字符串为 "a3c3" ，长度是 4 。

# 示例 2：
# 输入：s = "aabbaa", k = 2
# 输出：2
# 解释：如果删去两个 'b' 字符，那么压缩后的字符串是长度为 2 的 "a4" 。

# 示例 3：
# 输入：s = "aaaaaaaaaaa", k = 0
# 输出：3
# 解释：由于 k 等于 0 ，不能删去任何字符。压缩后的字符串是 "a11" ，长度为 3 。
 

# 提示：
# 1 <= s.length <= 100
# 0 <= k <= s.length
# s 仅包含小写英文字母


# @lc code=start
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        '''
        # 题意：从字符串中，选取T = n - k字符，使编码长度最小。
        # dp[p][cnt]表示从字符串的第p位开始，当前已经选取了cnt个字符。
        # 可以从当前的位置 p 开始向后遍历，只要发现后面有字符和 s[p] 相等，则选取。
        # 可以枚举选取的字符数量，进行状态转移。
        # 比如，字符串 s = ‘aabaaca’, p = 0。则我们可以从位置 0 开始，选取一个a（a abaaca），两个a(aa baaca)...知道五个a(aa b aa c a)然后再在之后的字符串中选取字符。
            # 形式化的转移方程：dp[p][cnt] = min(calc(same) + dp[j + 1][cnt + same])
            # 其中same表示s[p:j]中和s[p]相等的字符数量；calc(x)长度为 xx 的连续字符的编码长度。
            # dp[p][cnt] = min(dp[p][cnt], dp[p + 1][cnt])  初始条件：dp[n][T] = 0
        '''
        calc = lambda x : 1 if x == 1 else (2 if x < 10 else (3 if x < 100 else 4))
        s = list(s)
        n = len(s)
        T = n - k
        dp = [[1e9] * (T + 1) for _ in range(n + 1)]
        dp[n][T] = 0

        for p in range(n - 1, -1, -1):
            for cnt in range(T + 1):
                # 1.从此开始选择连续的字符
                same = 0
                for j in range(p, n):
                    same += (s[j] == s[p])
                    if (same + cnt > T): break
                    dp[p][cnt] = min(dp[p][cnt], calc(same) + dp[j + 1][cnt + same])
                dp[p][cnt] = min(dp[p][cnt], dp[p + 1][cnt])
        
        return dp[0][0]

# @lc code=end

