#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 排序(sort)?，优先队列(heapq)?，设计（collections.Counter）
        # 中间间隔的单位时间可以用来安排别的任务，也可以处于“待命”状态。
        res = 0
        task_map = collections.Counter(tasks)
        max_task_count = task_map.most_common(1)[0][1]
        res = (max_task_count - 1) * (n + 1)
        for k in task_map.values():
            if k == max_task_count:
                res += 1
        return res if res >= len(tasks) else len(tasks)
# @lc code=end

