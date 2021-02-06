#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        # 1.调用系统函数进行排序，Python中是归并和插入；其他语言--快排？  sort-array ; sorted-str
        s = sorted(s)
        t = sorted(t)
        return s == t
        '''
        # 2.计数排序，将char放在map中排，或者放在一个数组里，下标0-255之间，计数每个字母出现了多少次
        arr1, arr2 = [0] * 26, [0] * 26
        for i in s:
            arr1[ord(i)-ord('a')] += 1
        for j in t:
            arr2[ord(j)-ord('a')] += 1
        return arr1 == arr2
        '''
        dict1, dict2 = {}, {}
        for i in s:
            dict1[i] = dict1.get(i, 0) + 1
        for j in t:
            dict2[j] = dict2.get(j, 0) + 1
        # print(dict1, dict2)
        return dict1 == dict2
        '''
# @lc code=end

