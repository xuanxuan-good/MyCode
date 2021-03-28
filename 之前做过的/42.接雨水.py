#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        volume = 0
        left, right = 0, len(height) - 1
        l_max, r_max = height[left], height[right]
        while left < right:
            l_max, r_max = max(height[left], l_max), max(height[right], r_max)
            if l_max <= r_max:
                volume += l_max - height[left]
                left += 1
            else:
                volume += r_max - height[right]
                right -= 1
        return volume

        length = len(height)
        if length < 3: return 0
        res, idx = 0, 0
        stack = []
        while idx < length:
            while len(stack) > 0 and height[idx] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0: break
                h = min(height[stack[-1]], height[idx]) - height[top]
                dist = idx - stack[-1] - 1
                res += dist * h
            stack.append(idx)
            idx += 1
        return res
# @lc code=end

