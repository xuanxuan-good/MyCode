#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 2.按计数分类  O(NK) O(NK) 60ms 74%
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0]*26
            for i in s:
                count[ord(i)-ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
        '''
        # 1.排序数组分类 O(NKlogK) O(NK) 68ms 46%
        ans = collections.defaultdict(list)
        for i in strs:
            ans[tuple(sorted(i))].append(i)
        return list(ans.values())
        '''
        '''
        # 差别 - .get [] [s]  80ms 24%
        ans = {}
        for s in sorted(strs):
            ans[tuple(sorted(s))] = ans.get(tuple(sorted(s)), []) + [s]
        return list(ans.values())
        '''
# @lc code=end

