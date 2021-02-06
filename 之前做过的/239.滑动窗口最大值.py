#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 2.双端队列  单调减 存入索引
        # ①while当前元素大于单调队列中的尾端元素，则弹出尾端元素， 再加入当前元素 ②弹出不在窗口中的索引  ③只要开始形成窗口就每次放入res中
        queue = collections.deque()
        res = []
        for i in range(len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if queue[0] <= i-k:
                queue.popleft()
            if i >= k-1:
                res.append(nums[queue[0]])
        return res
        '''
        # 1.暴力枚举每一个窗口，找每一个窗口[n-k+1个]的最大，O(kn) O(n)   
            # sys.maxsize() 系统 较大的值
        res = []
        for i in range(len(nums)-k+1):
            cur = -sys.maxsize
            for j in range(i, i+k):
                cur = max(cur, nums[j])
            res.append(cur)
        return res
        '''
# @lc code=end

