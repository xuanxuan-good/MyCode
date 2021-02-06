#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#

# @lc code=start
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # 1.暴力 O(n^3)  每次枚举计算A[i:]和B[j:]的最长公共前缀k，最终答案是所有k中最大值
        # 2.dp 优化 使得任意一对A[i]和B[j]都只被比较一次； O(mn) O(mn)
        # dp[i][j]表示A[i:]和B[j:]的最长公共前缀，return max(dp[i][j])
        # dp[i][j] = dp[i+1][j+1] + 1 if A[i] = B[j] else 0
        # 3.滑动窗口√，重复子数组在两个数组中的位置可能不同（会比较多次的原因）；O((N+M)*min(N,M)) O(1)
        # 但是如果知道开始位置，就可以将A与B对齐，之后就可以对两个数组进行一次遍历，得到子数组的长度
        # 4.二分+hash
        def maxLength(addA, addB, length):
            ret = k = 0
            for i in range(length):
                if A[addA+i] == B[addB+i]:  # 找相对位置相同的重复子数组
                    k += 1
                else:
                    k = 0
                ret = max(ret, k)
            return ret
        n, m = len(A), len(B)
        ret = 0
        for i in range(n):  # 针对A，B不变，A的每个元素与B中的首元素对齐
            length = min(m, n-i)  # 取最小长度，为了不越界
            ret = max(ret, maxLength(i, 0, length))
        for j in range(m):  # 针对B，A不变，B的每个元素与A中的首元素对齐
            length = min(n, m-j)
            ret = max(ret, maxLength(0, j, length))
        return ret
        '''
        m, n = len(A), len(B)
        ans = 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = dp[i+1][j+1] + 1 if A[i] == B[j] else 0
                ans = max(ans, dp[i][j])
        return ans
        '''
# @lc code=end

