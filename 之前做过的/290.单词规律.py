#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ch2word, word2ch = {}, {}
        words = s.split(' ')
        # print(words)
        if len(words) != len(pattern):
            return False
        for ch, word in zip(pattern, words):
            if (ch in ch2word and ch2word[ch] != word) or (word in word2ch and word2ch[word] != ch):
                return False
            ch2word[ch] = word
            word2ch[word] = ch
        return True
# @lc code=end

