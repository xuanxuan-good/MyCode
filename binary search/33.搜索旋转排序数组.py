#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
# 给你一个整数数组 nums ，和一个整数 target 。
# 该整数数组原本是按升序排列，但输入时在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] ）。
# 请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

 
# 示例 1：
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4

# 示例 2：
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1

# 示例 3：
# 输入：nums = [1], target = 0
# 输出：-1
 

# 提示：
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums 中的每个值都 独一无二
# nums 肯定会在某个点上旋转
# -10^4 <= target <= 10^4


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0: return -1
        left, right = 0, n - 1
        while left < right:
            mid = left + right + 1 >> 1
            # 当中间元素严格小于右边元素的时候，[mid, right]一定是有序的
            if nums[mid] < nums[right]:
                # 既然在此区间是有序的，那么target在[mid, right]区间的时候，向右边查找就行了，left=mid
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else: right = mid - 1
            # 题目中说可以假设数组中不存在重复元素，因此另一种情况就是nums[mid] > nums[right]
            else:
                # 为了保证mid的取值一致性，这里用了mid-1，其实mid也是可以的
                if nums[left] <= target <= nums[mid - 1]:
                    right = mid - 1
                else: left = mid
        if nums[left] == target:
            return left
        return -1
# @lc code=end

