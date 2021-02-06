#
# @lc app=leetcode.cn id=649 lang=python3
#
# [649] Dota2 参议院
#

# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = collections.deque()
        dire = collections.deque()
        for i, ch in enumerate(senate):  # 分别记录每一次出现的位置，
            if ch == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            if radiant[0] < dire[0]:  # 在前边的 有权利进入下一轮移到后边
                radiant.append(radiant[0]+n)
            else:
                dire.append(dire[0]+n)
            radiant.popleft()  # 被移走或者进入下一轮
            dire.popleft()
        return "Radiant" if radiant else "Dire"
# @lc code=end

