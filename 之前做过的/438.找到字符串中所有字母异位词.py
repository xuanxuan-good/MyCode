#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # s: "cbaebabacd" p: "abc"
        # 1.s从前到后，每次遍历p的长度，看是否是异位词，是就把索引加入
        # 2.优化，map，出窗口的减掉，进窗口的加进来？看是不是异位词
        '''
        分别建立p和s[len(p)-1]的Counter;
        滑动窗口的形式 len(p)-1开始，向后遍历s
        s的对应索引的值 在Counter中+1
        判断Counter相等，则是异位词；结果中加入起始的索引i-len(p)+1
        加完之后，s对应位置的值-=1; 减完是0的再删除掉
        返回res
        '''
        res = []
        pCounter = collections.Counter(p)
        sCounter = collections.Counter(s[:len(p)-1])
        for i in range(len(p)-1, len(s)):
            sCounter[s[i]] += 1
            if sCounter == pCounter:
                res.append(i-len(p)+1)
            sCounter[s[i-len(p)+1]] -= 1
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]
        return res
# @lc code=end

