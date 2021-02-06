#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = nodeInsert = head
        while head and head.next:
            if head.val > head.next.val:  # 当前结点的值小，需要找合适位置插入
                nodeInsert = head.next  # 插入的结点
                pre = dummy  # 已排序部分，只要要插入的点大，继续遍历已排序部分
                while pre.next.val < nodeInsert.val:
                    pre = pre.next
                head.next = nodeInsert.next  # insertnode 删除    # 插入  head.next后移 相当于删除
                nodeInsert.next = pre.next
                pre.next = nodeInsert
            else:
                head = head.next  # 后边的值大，不需要找位置插入，保持原位置即可
        return dummy.next
# @lc code=end

