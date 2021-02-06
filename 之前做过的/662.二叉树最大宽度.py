#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # 1.bfs 按层序进行遍历，queue存放每一层所有的number和node，计算宽度就是queue头部的number和尾部的number相减
        width = 0
        queue = [(1, root)]
        while queue:
            temp = []
            width = max(width, queue[-1][0] - queue[0][0] + 1)
            for number, node in queue:
                for child in enumerate((node.left, node.right), 2*number):
                    if child[1]:
                        temp.append(child)
            queue = temp
        return width
        
        '''
        # dfs 深度优先遍历 每一个节点会记录自己的位置，对于每一深度先到达的节点位置记录在left[depth]中，则最大宽度就是pos-left[depth]+1
        self.ans = 0
        left = {}
        def dfs(root, depth=0, pos=0):
            if root:
                left.setdefault(depth, pos)  # 因为深度优先先从最左侧开始遍历，最开始setdefault的depth值，就是 每一深度先到达的节点位置，所以之后left[depth]是有值的，不需要再设置默认值pos
                self.ans = max(self.ans, pos-left[depth]+1)
                dfs(root.left, depth+1, 2*pos)
                dfs(root.right, depth+1, 2*pos+1)
        dfs(root)
        return self.ans
        '''
# @lc code=end

