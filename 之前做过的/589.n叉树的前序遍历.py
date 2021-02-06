#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # recursion 48ms 99%
        if not root:
            return []
        res = [root.val]
        for child in root.children:
            res.extend(self.preorder(child))
        return res

        '''
        # iterative 60ms 84%
        if root is None:
            return []
        stack = [root, ]
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children[::-1])
        return res
        '''
# @lc code=end

