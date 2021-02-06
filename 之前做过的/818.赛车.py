#
# @lc app=leetcode.cn id=818 lang=python3
#
# [818] 赛车
#

# @lc code=start
class Solution:
    def racecar(self, target: int) -> int:
        # bfs
        #1. Initialize double ended queue as 0 moves, 0 position, +1 velocity
        q = collections.deque([(0, 0, 1)])
        best = float('inf')
        while q:

            #(m) moves made, (p) position, (v) velocity
            m, p, v = q.popleft()

            if p == target:
                best = min(best, m)

            if m >= best:
                continue

            #2. Always consider moving the car in the direction it is already going
            q.append((m+1, p+v, 2*v))

            #3. Only consider changing the direction of the car if one of the following conditions is true
            #   i.  The car is driving away from the target.
            #   ii. The car will pass the target in the next move.  
            # v/abs(v)用来判断正负，如果速度为正，speed=-1，反之1
            if (p+v>target and v>0) or (p+v<target and v<0):
                q.append((m+1, p, -1*v/abs(v)))

        return best
# @lc code=end

