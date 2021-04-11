#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。


# 示例 1：
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]

# 示例 2：
# 输入：nums = [2,0,1]
# 输出：[0,1,2]

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 荷兰国旗问题
        return self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort(self, nums, left, right):
        if left >= right:
            return
        mid = left + right >> 1
        nums[mid], nums[left] = nums[left], nums[mid]
        x = nums[left]  # 所取的基准值,在最左边
        lt, rt, i = left - 1, right + 1, left
        # < =  >  left维护小于基准区间最后一个元素，right维护大于基准区间第一个元素，i维护的是等于基准区间的最后一个元素
        while i < rt:
            # 如果当前元素小于基准值，说明应该交换到左侧，
            # 因为左侧已经是基准值了，所以交换之后i位置对应的就是基准值，应该+1向后判断其他元素
            if nums[i] < x:
                lt += 1
                nums[lt], nums[i] = nums[i], nums[lt]
                i += 1
            # 当前元素大于基准值，说明应该交换到右侧，
            # i处交换成了右侧未知的一个值，因此还要判断当前位置的元素，不需要+1
            elif nums[i] > x:
                rt -= 1
                nums[rt], nums[i] = nums[i], nums[rt]
            # 相等的情况继续向后遍历即可
            else:
                i += 1
        # 找到 < > 两种情况的边界值lt, rt
        self.quick_sort(nums, left, lt)
        self.quick_sort(nums, rt, right)
# @lc code=end

