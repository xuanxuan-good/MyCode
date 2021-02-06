#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 1.暴力：直接枚举，从最小的单词看，看自己和自己的前缀，是不是其他单词的前缀  O(N^2 M) M是单词的平均长度
        # 2.把字符串对齐排在一起，找第1列...是否相同，当出现有一列不相同的时候，停止
        if not strs: return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
        '''
        # 按列1 48ms 26.5%
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix
        '''
        # 3.trie树，把所有单词放在trie里，然后在trie中看最长前缀在什么位置
        # 4.比较大小的方法
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, ch in enumerate(s1):
            if s2[i] != ch:
                return s1[:i]
        return s1
# @lc code=end

