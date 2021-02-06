#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # sum -> itreative
        a = collections.Counter(secret) & collections.Counter(guess)
        bulls = sum([i == j for i, j in zip(secret, guess)])
        return "%sA%sB" % (bulls, sum(a.values())-bulls)
# @lc code=end

