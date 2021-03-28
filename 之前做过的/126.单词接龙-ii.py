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
                    # 用（）的生成的是生成器，用extend可以提前计算出大小，效率更高
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i] + c + w[i+1:]
                            if neww in wordList:
                                new_layer[neww] += [j + [neww] for j in layer[w]]
                                #如果当前变化后的单词在wordlist中，那么是一种变化方法，将它加在之前已经有的单词列表之后  e.g.
                                # defaultdict(<class 'list'>, {'hot': [['hit', 'hot']]})
                                # defaultdict(<class 'list'>, {'dot': [['hit', 'hot', 'dot']]})
            # 防止已经变化的单词再遇到，重复会增多计算次数
            wordList -= set(new_layer.keys())
            layer = new_layer
        return res
# @lc code=end

