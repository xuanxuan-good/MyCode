#
# @lc app=leetcode.cn id=1030 lang=python3
#
# [1030] 距离顺序排列矩阵单元格
#

# @lc code=start
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # 枚举所有点时，我们可以直接按照哈曼顿距离分桶。这样我们就可以实现线性的桶排序。O(RC) O(RC)
        maxDist = max(r0, R-1-r0) + max(c0, C-1-c0)
        bucket = collections.defaultdict(list)
        dist = lambda r, c, r0, c0 : abs(r-r0) + abs(c-c0)

        for i in range(R):
            for j in range(C):
                bucket[dist(i, j, r0, c0)].append((i, j))
        res = []
        for i in range(maxDist+1):
            res.extend(bucket[i])
        return res

        '''
        # 调用sort 按曼哈顿距离 排序矩阵单元格 160ms 95% O(RClog(RC)) O(log(RC))
        res = [(i, j) for i in range(R) for j in range(C)]
        res.sort(key = lambda x:abs(x[0]-r0) + abs(x[1]-c0))
        return res
        '''
# @lc code=end

