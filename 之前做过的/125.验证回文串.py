#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 只考虑数字和字符，可以忽略大小写
        '''
        # 1.筛选+判断 O(s) O(s) 对字符串进行一次遍历，数字和字母放到另一个字符串sgood中，之后只要判断sgood是否是回文串即可
        #   判断是否是回文的两种方式：① 用字符串翻转的API得到逆序字符串，与正序相同则是回文
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        # print(sgood)
        return sgood == sgood[::-1]
        '''

        '''
        #       ② 双指针。两侧向内移动，判断字符都相同，且最后两指针相遇，说明是回文
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        left, right = 0, len(sgood)-1
        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left += 1
            right -= 1
        return True
        '''

        # 2.原字符串上直接判断 O(s) O(1) 双指针，每次要移动到下一个字母或数字，再判断是否相同
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():  # str.lower()转换为小写字母
                    return False
                left += 1
                right -= 1
        return True
# @lc code=end

