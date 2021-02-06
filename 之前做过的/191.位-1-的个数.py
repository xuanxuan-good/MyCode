#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
    # 大部分情况 需要移动32次    
        # 1.for loop 0->32 count += 1
        # %2[看最后一位是否是一] /2[去掉最后一位]
        # &1, x = x >> 1
    # 4.x = x & (x-1)  每次清零最低位的1，判断x是否为0
    # 每次清空，判断x>0的情况下，count++；；x每次打掉最后一位的1，直到x变为0，退出就行了
        count = 0
        while n > 0:
            n = n & (n-1)
            count += 1
        return count

        # return bin(n).count('1')

        '''
        count = 0
        while n:
            res = n % 2
            if res == 1:
                count += 1
            n //= 2
        return count
        '''

        '''
        count = 0
        while n:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count
        '''
# @lc code=end 

