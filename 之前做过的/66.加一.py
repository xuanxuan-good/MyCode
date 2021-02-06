#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        # str和int转换 36ms 88%
        stra = [str(i) for i in digits]
        # print(stra)
        intb = int(('').join(j for j in stra)) + 1
        # print(intb)
        result = [int(r) for r in str(intb)]
        return result
        '''
        # logic 36ms  88%
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0,1)
        return digits
# @lc code=end

