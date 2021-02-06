#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        # 1.穷举：loop s -> 1,length: loop i -> 1,length  s+i % A.lenght - index
        # 2.判断子串：A.length == B.length && (A+A).contains(B) O(n^2)
            # contains 源代码：for 第一个s对应上之后 for 判断之后是否对应
        # 3.Rabin-Karp 字符串哈希 判断两字符串哈希值是否相等-O(n) O(n)
        # 4.KMP
        return len(A) == len(B) and  B in A+A
# @lc code=end

