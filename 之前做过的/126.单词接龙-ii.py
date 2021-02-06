#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 代码学习
        wordList = set(wordList)
        res = []
        layer ={}
        layer[beginWord] = [[beginWord]]
        while layer:
            new_layer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i] + c + w[i+1:]
                            if neww in wordList:
                                new_layer[neww] += [j + [neww] for j in layer[w]]
            wordList -= set(new_layer.keys())
            layer = new_layer
        return res
# @lc code=end

