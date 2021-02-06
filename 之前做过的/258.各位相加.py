#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            temp = 0
            while num != 0:
                temp += num % 10
                num = num // 10
            num = temp
        return num
        '''
        while num > 9:
            num = eval('+'.join(n for n in str(num)))
        return num
        '''
# @lc code=end

