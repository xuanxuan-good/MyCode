#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # dfs  60ms 62%
        res = []
        self.dfs(root, res, 0)
        return res
    def dfs(self, root, res, level):
        # terminator
        if not root:
            return []
        # current logic
        if level == len(res):
            res.append(root.val)
        # else:
        res[level] = max(res[level], root.val)
        # drill down
        self.dfs(root.left, res, level+1)
        self.dfs(root.right, res, level+1)
        # reverse current state
        '''
        # bfs 52ms 91%
        res = []
        level = [root]
        while root and level:
            res.append(max([node.val for node in level]))
            level = [n for kid in level for n in (kid.left, kid.right) if n]
        return res
        '''
# @lc code=end

