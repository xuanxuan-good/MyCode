#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickPow(n):
            ans = 1
            x_c = x  #当想要改变x的值时，只能复制给一个新的局部变量，该变量只在内嵌函数中起作用
            while n > 0:
                if n % 2 == 1:
                    ans *= x_c
                x_c *= x_c
                n = n // 2
            return ans
        return quickPow(n) if n >= 0 else 1 / quickPow(-n)
        '''
        # 1.暴力 loop 1-n: res*=x   n=0:1.0 n<0:1/ -n
        # 2.分治
        def fastPow(n):
            # terminator
            if n == 0:
                return 1.0
            # current logic
            # drill down
            y = fastPow(n//2)
            # reverse
            return y * y if n % 2 == 0 else y * y * x
        return fastPow(n) if n >= 0 else 1 / fastPow(-n)
        '''
        '''
        # iterative 二进制？
        def quickPow(n):
            ans = 1
            x_c = x
            while n > 0:
                if n % 2 == 1:
                    ans *= x_c
                x_c *= x_c  #? 为什么不能直接x
                n = n // 2
            return ans
        return quickPow(n) if n >= 0 else 1 / quickPow(-n)
        '''
# @lc code=end

