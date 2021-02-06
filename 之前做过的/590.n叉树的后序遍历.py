#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
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
    def postorder(self, root: 'Node') -> List[int]:
        # iterative 60 ms 83%
        res = []
        if not root:
            return []
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children)
        return res[::-1]
        '''
        # recursion  60 ms 83%
        res = []
        if not root:
            return []
        def recursion(root, res):
            for child in root.children:
                recursion(child, res)
            res.append(root.val)  #!!!
        recursion(root, res)
        return res
        '''
# @lc code=end

