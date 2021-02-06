#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] 矩形区域不超过 K 的最大数值和
#

# @lc code=start
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # 找矩阵内部 不大于k的 最大矩形和
        # 1.前缀和+排序  （滚动数组）
        row, col = len(matrix), len(matrix[0])
        res = float("-inf")
        for left in range(col):  #列  针对每一列
            nums = [0] * row  # 相当于每个竖着的一列 是一个nums 
            for right in range(left, col):  # 列  从right开始往后遍历列
                for i in range(row):  # 针对遍历的每一块  整行，列数不同
                    nums[i] += matrix[i][right]  # nums[i] 相当于把长方体的横向压缩，变成竖着一列的
                array = [0]
                cum = 0
                for num in nums:  # 针对处理好的nums，计算最大子序和，sum[i,j]=sum[0,j]（会后得到）-sum[0,i](会先得到)<=k  -> sum[0,j]-k 【x】 <= sum[0,i]
                    cum += num
                    loc = bisect.bisect_left(array, cum - k)  # 存在则返回cum-k所在的索引，不存在则返回比它小的左侧索引  cum - k -- sum[0,j]-k 比较找出比sum[0,i]小的最大值x
                    if loc < len(array):
                        res = max(res, cum - array[loc])  # cum是累加和，减去找到的不大于sum[0,i]的【x】值，得到的应该是一个比k小的res
                    bisect.insort(array, cum)  #插入  array -- sum[0,i]
        return res

        '''
        # 超出时间限制  25/27  2. 暴力+动态规划+状态压缩（四维 -> 二维）
        # 时间复杂度 O(m^2n^2)，空间复杂度 O(mn)  次更换左上角时就重复利用 dp，故只需记录右下角即可
        rows, cols = len(matrix), len(matrix[0])
        # maxs = -matrix[0][0]
        maxs = float("-inf")
        for i1 in range(1, rows+1):
            for j1 in range(1, cols+1):
                dp = [[0]*(cols+1) for _ in range(rows+1)]
                dp[i1][j1] = matrix[i1 - 1][j1 - 1]
                for i2 in range(i1, rows+1):
                    for j2 in range(j1, cols+1):
                        dp[i2][j2] = dp[i2 - 1][j2] + dp[i2][j2 - 1] - dp[i2 - 1][j2 - 1] + matrix[i2 - 1][j2 - 1]
                        if dp[i2][j2] <= k and dp[i2][j2] > maxs:
                            maxs = dp[i2][j2]
        return maxs
        '''
    '''  
  max = Integer.MIN_VALUE;  //java
    '''
# @lc code=end

