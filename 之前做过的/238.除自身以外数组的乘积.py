#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        # 1.左右乘积列表O(n) O(n)，构建前缀数组L 和 后缀数组R 以及结果数组answer[i]=L[i]*R[i] 
        [1,2,3,4]
         1 1,2,6    L   【range(0, 4-1) --> res.append(p) 前缀append 】
        24,12,4 1   R   【range(4-1, 0, -1) --< res[i-1] *= q 后缀相乘 】
        [24,12,8,6] answer nums[i] 前缀i-1与后缀i+1之积
        # 2.用一个结果数组直接乘即可 O(n) O(1)
        '''
        res, p, q = [1], 1, 1
        for i in range(len(nums) - 1): # bottom triangle
            p *= nums[i]
            res.append(p)
        for i in range(len(nums) - 1, 0, -1): # top triangle
            q *= nums[i]
            res[i - 1] *= q
        return res

# @lc code=end

