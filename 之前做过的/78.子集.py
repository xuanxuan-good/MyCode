#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if not nums:
            return ans
        def dfs(nums, ans, res, level):
            # terminator
            if level == len(nums):
                ans.append(res[:])  # res是引用，最后会全部被清空；要用res[:]
                # 因为如果只用res，append的是对同一个对象res的引用，最后这个引用会被清空
                return
            # current logic ; drill down
            dfs(nums, ans, res, level+1)
            res.append(nums[level])
            dfs(nums, ans, res, level+1)
            # reverse current state  回溯
            res.pop()
        dfs(nums, ans, [], 0)
        return ans
        '''
        # recursion  44ms 44% 回溯？
        res = []
        n = len(nums)
        def helper(i, tmp):
            # terminator
            res.append(tmp)
            # current logic ; drill down
            for j in range(i, n):
                helper(j+1, tmp+[nums[j]])  
        helper(0, [])
        return res
        '''
        '''
        # 2. 库函数  40ms 70%
        res = []
        for i in range(len(nums)+1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res
        '''
        '''
        # 1.iterative  36ms 87%
        res = [[]]
        for i in nums:
            res += [[i] + c for c in res]
        return res
        '''
# @lc code=end

