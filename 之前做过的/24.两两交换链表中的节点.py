#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # recursion  44ms;47%
        if not head or not head.next:
            return head
        nxt = head.next
        head.next = self.swapPairs(head.next.next)
        nxt.next = head
        return nxt
        '''
        # iterative 64ms 9%
        if not head or not head.next:
            return head
        prev = ListNode(0)
        prev.next = head
        dummy = prev  #为了指向头结点，通过dummy找到改变后的链表
        while head and head.next:
            first = head
            second = head.next
            # swap
            prev.next = second
            first.next = second.next
            second.next = first
            # 重新赋值
            prev = first
            # print(prev)  #143;3
            head = first.next
            # print(dummy.next)  #2134;2143
        return dummy.next
        '''
# @lc code=end

