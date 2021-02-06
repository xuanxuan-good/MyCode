#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # 双向bfs
        if end not in bank:
            return -1
        beginSet = {start}
        endSet = {end}
        visited = set()
        bank = set(bank)
        dist = 0
        while beginSet:
            dist += 1
            next_begin = set()
            for word in beginSet:
                for i in range(8):
                    for c in 'ACGT':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in endSet:
                            return dist
                        if new_word in bank and new_word not in visited:
                            visited.add(new_word)
                            next_begin.add(new_word)
            beginSet = next_begin
            if len(endSet) < len(beginSet):
                endSet, beginSet = beginSet, endSet
        return -1
        
        '''
        # bfs
        if end not in bank:
            return -1
        visited = set()
        queue = collections.deque([(start, 0)])  # 发生了几次变化 与单词接龙中的最短转换序列长度 不同
        while queue:
            word, step = queue.popleft()
            if word == end:
                return step
            for i in range(len(word)):
                for c in 'ACGT':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in bank and next_word not in visited:
                        visited.add(next_word)
                        queue.append([next_word, step+1])
        return -1
        '''
# @lc code=end

