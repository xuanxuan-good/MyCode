#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 2.从后遍历  end>0 beg>=0
        end = len(s)-1
        while end > 0 and s[end] == " ":
            end -= 1
        beg = end
        while beg >= 0 and s[beg] != " ":
            beg -= 1
        return end - beg
        '''
        # 1.直接split -1
        arr = s.split()
        if not arr:
            return 0
        return len(arr[-1])
        '''
# @lc code=end

