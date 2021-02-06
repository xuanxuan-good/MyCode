#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # 1.split, reverse, join [python中strip()可以去除首尾空格或换行符]
        arr = s.split()
        return " ".join(arr[::-1])

        '''
        # 2.reverse 整个string， 然后再单独reverse每个单词 [列表可以反转，字符串不能]
        a = list(s)
        l, r = 0, len(a)-1
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
        arr = "".join(a).split()
        res = []
        # print(arr)
        for i in arr:
            res.append("".join(list(i)[::-1]))
        return " ".join(res)
        '''
# @lc code=end

