#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 1.暴力 i枚举所有字符，j针对每个字符枚举看是否是唯一的 O(n^2)
        # 2.java-map(hashmap-hash, treemap-bst)  hash O(n)
        ss = collections.Counter(s)
        for inde, i in enumerate(s):
            if ss[i] == 1:
                return inde
        return -1
        
        '''
        dicts = {}
        for i in s:
            dicts[i] = dicts.get(i, 0) + 1
        # print(dicts)
        for ind, i in enumerate(s):
            if dicts[i] == 1:
                return ind
        return -1
        '''
# @lc code=end

