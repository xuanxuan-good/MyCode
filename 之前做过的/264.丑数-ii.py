#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Ugly:
    def __init__(self):
        seen = {1,}
        self.nums = nums = []
        heap = []
        heapq.heappush(heap, 1)
        for _ in range(1690):
            curr_ugly = heapq.heappop(heap)
            nums.append(curr_ugly)
            for i in [2,3,5]:
                new_ugly = curr_ugly * i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
class Solution:
    u = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        # heap
        return self.u.nums[n-1]

        '''
        # heap
        ugly = [1]
        seen = set()  #集合，与字典类似;存放key值不重复
        seen.add(1)
        for _ in range(n):
            curr_ugly = heapq.heappop(ugly)
            for i in [2, 3, 5]:
                new_ugly = i * curr_ugly
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(ugly, new_ugly)
        return curr_ugly
        '''

        '''
        # 动态规划
        ulgy = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ulgy[i2], 3 * ulgy[i3], 5 * ulgy[i5]
            umin = min(u2, u3, u5)
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ulgy.append(umin)
            n -= 1
        return ulgy[-1]
        '''
# @lc code=end

