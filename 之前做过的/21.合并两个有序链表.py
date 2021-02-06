#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # recursion
        # if not l2:
        #     return l1
        # elif not l1:
        #     return l2
        #在纯and语句中，如果每一个表达式都不是假的话，那么返回最后一个，因为需要一直匹配直到最后一个。
        # 如果有一个是假，那么返回假
        if not l1 or not l2:  # 40ms 96%
            return l1 or l2
         # 在纯or语句中，只要有一个表达式不是假的话，那么就返回这个表达式的值。
         #只有所有都是假，才返回假
        elif l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        '''
        # iterative 40ms 96%
        prevhead = ListNode(-1)  #哨兵prevhead
        prev = prevhead  #中间遍历过程用prev
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 else l2
        return prevhead.next
        '''
# @lc code=end

