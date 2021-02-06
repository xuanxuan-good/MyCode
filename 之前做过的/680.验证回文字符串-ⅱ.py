#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 最多删除一个字符的情况，是否可以构成回文串
        # 1.暴力，逐个删除字符，再遍历判断是否回文O(N^2)
        '''
        # 2.双指针，当碰到有不相等的时候，删除左边或者右边，再判断剩下的是否是回文
        isPalindrome = lambda x : x == x[::-1]
        strPart = lambda s, x : s[:x] + s[x+1:]
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(strPart(s,left)) or isPalindrome(strPart(s, right))
            left += 1
            right -= 1
        return True
        '''

        '''
        # 3.改进版双指针，被删除字符的两边不需要再判断，只要判断中间是否是回文即可 即(left, right] or [left, right)
        isPalindrome = lambda x : x == x[::-1]
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(s[left:right]) or isPalindrome(s[left+1:right+1])
            left += 1
            right -= 1
        return True
        '''

        # 4.贪心+双指针 [和3相同，只是x[::-1]换一种原地写法，使得空间复杂度降为O(1)]  !!!索引位置
        def isPalindrome(left, right):
            l, r = left, right
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(left, right-1) or isPalindrome(left+1, right)
            left += 1
            right -= 1
        return True
# @lc code=end

