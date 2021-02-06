#
# @lc app=leetcode.cn id=641 lang=python3
#
# [641] 设计循环双端队列
#

# @lc code=start
class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
# learn code
class MyCircularDeque:  #80ms 91%

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head, self.tail = None, None
        self.count = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        node = Node(value)
        if self.count == self.capacity:
            return False
        elif self.count == 0:
            self.head = node
            self.tail = self.head
        else:       
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        node = Node(value)
        if self.count == self.capacity:
            return False
        elif self.count == 0:
            self.head = node
            self.tail = self.head
        else:    
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True


    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        Thanks to the self.prev pointer of double LinkedList, the complexity is O(1).
        """
        if self.count == 0:
            return False
        self.tail = self.tail.prev
        self.count -= 1
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.count == 0:
            return -1
        return self.head.value
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.count == 0:
            return -1
        return self.tail.value
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.count == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

