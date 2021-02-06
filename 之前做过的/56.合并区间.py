#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 如果结果数组为空，或者结果数组右边的值 小于 当前interval，可以加入结果中(与上一区间不重合)
        # 否则，右侧界限要取最大值（与上一区间有重合）
        intervals.sort(key=lambda x: x[0])  #！！！
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
# @lc code=end

