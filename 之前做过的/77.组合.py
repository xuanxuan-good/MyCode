#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # traceback
        if n == 0 or k == 0:
            return [[]]
        res, ans = [], []
        self.dfs(list(range(1, n+1)), k, res, ans)
        return ans
        
    def dfs(self, nums, k, res, ans):
        # terminator
        if k == len(res):
            ans.append(res[:])
            return
        # current logic
        for i in range(len(nums)):
            res.append(nums[i])
        # drill down
            self.dfs(nums[i+1:], k, res, ans)
        # reverse
            res.pop()
        '''
        # recursion
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]  #pre这里相当于一种剪枝
        # n个数中取k个数的组合，在第k个数到最后一个数 中取任意一个数， 作为第k个数，
        # 之前的1到k-1个数有自己本身上一层函数产生
        '''

        '''
        #  4.reduce
        return reduce(lambda C, _: [[i]+c for c in C for i in range(1, c[0] if c else n+1)], range(k), [[]])
        '''

        '''
        # 3.iterative
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
        return combs
        '''
        
        '''
        # 1.库函数
        return list(itertools.combinations(range(1, n+1), k))
        '''
# @lc code=end

