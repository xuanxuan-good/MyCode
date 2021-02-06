#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 2.正向查找所在位置
        maxPos, end, step = 0, 0, 0
        for i in range(len(nums)-1):  #如果遍历最后一位，正好在最后位置的时候会增加一次跳跃次数
            maxPos = max(maxPos, nums[i]+i)
            if i == end:
                end = maxPos
                step += 1
        return step
        '''
        # 1.反向查找所在位置 O(n^2) O(1)
        position = len(nums)-1
        step = 0
        while position > 0:
            for i in range(len(nums)):
                if nums[i]+i >= position:
                    position = i
                    step += 1
                    break
        return step
        '''
# @lc code=end

