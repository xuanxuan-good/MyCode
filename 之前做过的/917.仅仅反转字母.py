#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        # "ab-cd"
        '''
        # 1.字母栈：遍历S，字母放入栈；再次遍历，是字母就弹出，不是就加入本身符号 O(n) O(n)
        leters = [c for c in S if c.isalpha()]
        # print(leters)  # ['a', 'b', 'c', 'd']
        res = []
        for i in S:
            if i.isalpha():
                res.append(leters.pop())
            else:
                res.append(i)
        return "".join(res)
        '''

        # 2.反转指针 维护一个指针j从后往前遍历字符串，当需要字母时就使用它。[是字母就加入交换的，不是字母就直接加入]
        res = []
        j = len(S) - 1
        for ch in S:
            if ch.isalpha():
                while not S[j].isalpha():
                    j -= 1
                res.append(S[j])
                j -= 1
            else:
                res.append(ch)
        return "".join(res)
# @lc code=end

