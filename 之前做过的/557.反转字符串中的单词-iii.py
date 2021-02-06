#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # tsetnoc edoCteeL ekat s'teL
        # 整个字符串与每个单词间的关系
        '''
        # 1.字符串分割成单词列表，再对每一个列表反转 O(n)
        # print(s.split(" "))  # ["Let's", 'take', 'LeetCode', 'contest']
        return " ".join(word[::-1] for word in s.split(" "))
        '''

        '''
        # 2.分割的单词列表反转，再整个字符串反转 O(n)
        # print(s.split(" ")[::-1])  # ['contest', 'LeetCode', 'take', "Let's"]
        return " ".join(s.split(" ")[::-1])[::-1]
        '''

        # 3.先对整体字符串进行反转，再反转单词列表 O(n)
        # print(s[::-1])  # tsetnoc edoCteeL ekat s'teL
        return " ".join(s[::-1].split()[::-1])  # "s'teL ekat edoCteeL tsetnoc"
# @lc code=end

