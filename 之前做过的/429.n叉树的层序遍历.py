#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # BFS
        if not root:
            return []
        res = []
        queue = collections.deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)  #children 不止一个
            res.append(level)
        return res
        '''
        # 队列 BFS
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            res.append(node.val for node in queue)
            queue = [child for node in queue for child in node.children]
        return res
        '''
# @lc code=end

