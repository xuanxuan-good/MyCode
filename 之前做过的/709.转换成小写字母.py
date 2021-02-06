#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#

# @lc code=start
class Solution:
    def toLowerCase(self, str: str) -> str:
        # 大写字母ASCII码值是65-90；小写字母ASCII码值是97-122 相差32 c |= 32(0010 0000)
        # 或|32，就相当于是把倒数第6位置1，也就是+32
        # return str.lower()
        res = ""
        for s in str:
            if 'A' <= s <= 'Z':
                res += chr(ord(s)|32)
            else:
                res += s
        return res
# @lc code=end

