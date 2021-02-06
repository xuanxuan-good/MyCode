#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:  # 
            return 0
        # 双向BFS ，与单向bfs的差距就是不用queue了，而是用两个set来表示；在判断新生成的new_word是不是在另一个扩散的set里时 比较方便  100ms  [bfs 500ms]
        beginSet = {beginWord}
        endSet = {endWord}
        dist = 1  # 走的步数
        wordList = set(wordList)  # 方便查找，set的时间复杂度O(1)--list的O(n)
        visited = set()
        word_len = len(beginWord)
        # bfs starts here
        while beginSet:  # 与beginSet and endSet是一样的，因为最后边两个set会按照长度大小进行互换，begin始终是较小的，只要begin不为零即可
            dist += 1
            next_front = set()  # Java中的temp，后边扩散的点要放到next_front中去
            for word in beginSet:  # beginSet中每一个单词的每一个字母遍历一遍
                for i in range(word_len):
                    for c in string.ascii_lowercase:  # ☆ 'a'~'z'
                        if c != word[i]:  # 和当前单词不重复再考虑生成新词
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in endSet:  # 从beginSet里扩散的new_word在endSet中可以找到，说明相交了
                                return dist
                            if new_word in wordList and new_word not in visited:
                                visited.add(new_word)
                                next_front.add(new_word)  # 逐渐把下一次要扩散的单词都纷纷放到next_front中
            beginSet = next_front  # 当beginSet里全部处理完了，next_front就准备好了要给新的beginSet
            if len(endSet) < len(beginSet):
                beginSet, endSet = endSet, beginSet
        return 0

        '''
        # bfs
        visited = set()
        wordList = set(wordList)
        queue = collections.deque([(beginWord, 1)])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList and next_word not in visited:
                        visited.add(next_word)
                        queue.append([next_word, length+1])
        return 0
        '''
# @lc code=end

