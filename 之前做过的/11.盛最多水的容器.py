#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针
        l = 0; r = len(height)-1
        maxa = 0
        while l < r:
            if height[l] < height[r]:
                area = (r-l)*height[l]
                l += 1
            else:
                area = (r-l)*height[r]
                r -= 1
            if maxa < area:
                maxa = area
        return maxa
        '''
        # 一维数组的坐标变换；i，j
        # 1.枚举，left bar x, right bar y, (y-x)*height_diff
        # O(n^2)
        # 2.O(n)，左右边界i，j,向中间收敛
        # 移动较小的边才有可能使面积变大
        left = 0
        right = len(height)-1
        areamax = 0
        while left<right:
            if height[left]<height[right]:
                area = (right-left) * height[left]
                left += 1
            else:
                area = (right-left) * height[right]
                right -= 1
            if areamax<area:
                areamax = area
        return areamax
        '''
        '''
        l, r = 0, len(height)-1
        maxarea = 0
        while l<r:
            if height[l]<height[r]:
                minheight = height[l]
                l += 1
            else:
                minheight = height[r]
                r -= 1
            maxarea = max(maxarea, (r-l+1)*minheight)  #+1
        return maxarea
        '''
# @lc code=end

