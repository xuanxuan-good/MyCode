#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:
    # Python的动态实现方式
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}  # 结点结构 root定义了一个字典，表示用一个字典来表示，key是'a~z'这样的字符，value就是下一个结点的位置
        # 初始化时就把self.root弄好，之后向下走会不断地在字典里，一个嵌一个往下，把整个树形结构放在字典内
        self.end_of_word = '#'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # 循环这个word，对于里边的每个字符，去node里找有没有；如果有就直接拿出来node等于的；如果没有，要给它创建一个新的字典进去
        # 整个循环走完，就会把单词里的字符全部加到字典树中了
        # 最后会有一个标记位end_of_word，不然没法区分当前是只包含前缀，还是包含整个单词
        node = self.root
        for char in word:
            node = node.setdefault(char, {})  # setdefault与get差不多，区别是setdefault在没有找到key的值时，返回默认值并且会将 key：默认值 放到字典中
        node[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # 循环要查找的单词，每个字符去树的相应层里边的结点，查它有没有下一个结点
        # 如果没有则返回false，如果有在走下一个char所对应的下一个结点，找出来放到新的node中
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

