#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 快速排序
        self.quicksort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums))))
        # return "".join(map(str, nums)).lstrip("0") or "0"  #写法二

    def quicksort(self, nums, l, r):
        # terminator  #！！！
        if l >= r:
            return
        # process
        pos = self.partition(nums, l, r)
        self.quicksort(nums, l, pos-1)
        self.quicksort(nums, pos+1, r)  # 注意边界加一减一

    def partition(self, nums, l, r):
        low = l  # 
        while l < r:
            if self.compare(nums[l], nums[r]):
                nums[l], nums[low] = nums[low], nums[l]  # 
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]  #
        return low

    def compare(self, n1, n2):
        return str(n1)+ str(n2) > str(n2) + str(n1)

        '''
        # 排序？
        num = [str(x) for x in nums]
        num.sort(reverse = True)
        return ''.join(num).lstrip('0') or '0'
        '''
# @lc code=end

