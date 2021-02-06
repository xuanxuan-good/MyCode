#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # DFS 36ms 93%
        res = []
        self.dfs(root, res, 0)
        return res
    def dfs(self, root, res, level):
        # terminator
        if not root:
            return []
        # current logic
        if level >= len(res):
            res.append([])
        res[level].append(root.val)
        # drill down
        self.dfs(root.left, res, level+1)
        self.dfs(root.right, res, level+1)
        # reverse current logic
        '''
        # BFS  36ms 93%
        res = []
        level = [root]
        while root and level:
            res.append([node.val for node in level])
            level = [n for kid in level for n in (kid.left, kid.right) if n]
        return res
        '''
# @lc code=end

