#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        i = j = mx = d = 0
        directions, obstacles = [(0, 1), (-1, 0), (0, -1), (1, 0)], set(map(tuple, obstacles))
        for command in commands:
            if command == -2:
                d = (d+1) % 4
            elif command == -1:
                d = (d-1) % 4
            else:
                x, y = directions[d]
                while command and (i+x, j+y) not in obstacles:
                    i += x
                    j += y
                    command -= 1
            mx = max(mx, i**2 + j**2)
        return mx
# @lc code=end

