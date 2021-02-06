#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        # 到达第i级台阶的阶梯顶部的最小花费 有两个选择
        # 先踏上i-2级台阶（总花费dp[i-2]）,再迈两步踏上第i级台阶（花费cost[i]）
        # 先踏上i-1级台阶（总花费dp[i-1]）,再迈一步踏上第i级台阶（花费cost[i]）
        # 1.正推 dp[i] = min(dp[i-1], dp[i-2]) + cost[i] ；初始值dp[0] = cost[0];dp[1] = min(cost[0]+cost[1], cost[1])
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[-1], dp[-2])
        '''

        # 优化
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-2], cost[i-1])
        return min(cost[-1], cost[-2])

        '''
        # 到达第i级台阶的阶梯顶部的最小花费 有两个选择
        # 1.先付出最小总花费minCost[i-1]到达第i级台阶，同时花费cost[i]
        # 2.先付出最小总花费minCost[i-2]到达第i-1级台阶，同时花费cost[i-1]
        # 则最小总花费就是两者的最小值；初始值minCost[0] = min(0, cost[0]);minCost[1] = min(cost[0], cost[1])
        n = len(cost)
        dp = [0] * n
        dp[1] = min(cost[0], cost[1])
        for i in range(2, n):
            dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i-1])
        return dp[-1]
        '''

        '''
        # 空间优化
        n = len(cost)
        minCount0, minCount1 = 0, min(cost[0], cost[1])
        for i in range(2, n):
            minCount = min(minCount0+cost[i-1], minCount1+cost[i])
            minCount0, minCount1 = minCount1, minCount
        return minCount
        '''
# @lc code=end

