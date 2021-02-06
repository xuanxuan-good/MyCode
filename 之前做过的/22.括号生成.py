#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # dp
        dp = [[] for _ in range(n+1)]
        dp[0].append('')
        for i in range(n+1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i-1-j]]
        return dp[n]
        '''
        if n == 0:  
            return []
        total_l = []
        total_l.append([None])    # 0组括号时记为None
        total_l.append(["()"])    # 1组括号只有一种情况
        for i in range(2,n+1):    # 开始计算i组括号时的括号组合
            l = []  # temp
            for j in range(i):    # 开始遍历 p q ，其中p+q=i-1 , j 作为索引;;;p,q是一组对称的左右括号
                now_list1 = total_l[j]    # p = j 时的括号组合情况
                now_list2 = total_l[i-1-j]    # q = (i-1) - j 时的括号组合情况
                for k1 in now_list1:  
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        el = "(" + k1 + ")" + k2  # 括号内 和 括号外？
                        l.append(el)    # 把所有可能的情况添加到 l 中
            total_l.append(l)    # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
        return total_l[n]
        '''
        
        '''
        # 回溯递归
        res = []
        def generate(left, right, n, s):
            # terminator
            if left == n and right == n:
                res.append(s)
                return
            # current logic; drill down
            if left < n:
                generate(left+1, right, n, s+"(")
            if left > right:
                generate(left, right+1, n, s+")")
            # reverse current state
        generate(0, 0, n, "")
        return res
        '''
        # dfs,bfs
# @lc code=end

