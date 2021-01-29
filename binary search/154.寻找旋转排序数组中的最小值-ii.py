# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-l2rb6/
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 请找出其中最小的元素。
# 注意数组中可能存在重复的元素。

# 示例 1：
# 输入: [1,3,5]
# 输出: 1

# 示例 2：
# 输入: [2,2,2,0,1]
# 输出: 0

# 说明：
# 这道题是 寻找旋转排序数组中的最小值 的延伸题目。
# 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums) - 1
        while n > 0 and nums[n] == nums[0]:
            n -= 1
        # 放置位置的正确性，如果是[1,2,1]，则删除重复后，[1,2]不进行下边的判断就会一直向左找到右边的1
        if nums[0] < nums[n]: return nums[0]
        l, r = 0, n
        while l < r:
            mid = l + r >> 1
            if nums[mid] < nums[0]:
                r = mid
            else: l = mid + 1
        return nums[r]
# @lc code=end

