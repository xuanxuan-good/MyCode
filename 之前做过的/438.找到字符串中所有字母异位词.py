#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 双指针，滑动窗口，同类型题目：76，567，剑指48
        dictp = collections.Counter(p)
        window = {}
        left, right, res = 0, 0, []
        vaild = 0
        arrs = list(s)
        while (right < len(arrs)):
            c = arrs[right]
            right += 1
            if (c in dictp):
                window[c] = window.get(c, 0) + 1
                if dictp[c] == window[c]:
                    vaild += 1
            while (vaild == len(dictp.items())):
                if (right - left == len(p)):
                    res.append(left)
                d = arrs[left]
                left += 1
                if (d in dictp):
                    if dictp[d] == window[d]:
                        vaild -= 1
                    window[d] -= 1
        return res
# @lc code=end

