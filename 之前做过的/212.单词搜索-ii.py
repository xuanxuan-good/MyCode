#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1.words遍历--> board search  O(N*m*m*4^k) 单词个数，矩阵行列，四连通深搜 每个单词平均长度
        # 2.trie  a.all words --> 构建trie 使prefix可以高效查询
        #         b.board,dfs  遍历每一个字符，从起点开始dfs,dfs产生任何的字符串到words中查找，看是不是它的prefix,如果是并且最后存在就输出；否则不输出
        trie = {}  # 1.构造字典树 O(Nk)
        for word in words:  # N
            node = trie
            for char in word:  # k
                node = node.setdefault(char, {})
            node['#'] = True

        def dfs(i, j, node, pre, visited):  # (i,j)当前坐标，node当前trie树结点，pre前面的字符串，visited已访问坐标
            if '#' in node:  # 已有字典树结束
                res.add(pre)  # 添加答案
            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r, c = i+di, j+dj
                if -1 < r < h and -1 < c < w and board[r][c] in node and (r, c) not in visited:  # 可继续搜索
                    dfs(r, c, node[board[r][c]], pre+board[r][c], visited | {(r, c)})  # 2.dfs搜索

        res, h, w = set(), len(board), len(board[0])
        for i in range(h):  # 3.遍历board
            for j in range(w):
                if board[i][j] in trie:  # 可继续搜索
                    dfs(i, j, trie[board[i][j]], board[i][j], {(i, j)})  # dfs搜索  ！！！
        return list(res)
# @lc code=end

