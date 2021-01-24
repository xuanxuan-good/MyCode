#
# @lc app=leetcode.cn id=721 lang=python3
#
# [721] 账户合并
#给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该账户的邮箱地址。
# 现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
# 合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按字符 ASCII 顺序排列的邮箱地址。账户本身可以以任意顺序返回。


# 示例：
# 输入：
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# 输出：
# [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# 解释：
# 第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。 
# 第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
# 可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
# ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']] 也是正确的。


# 提示：
# accounts的长度将在[1，1000]的范围内。
# accounts[i]的长度将在[1，10]的范围内。
# accounts[i][j]的长度将在[1，30]的范围内。


# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        dfs找属于不同人的所有邮箱
        遍历每一个账户对应的所有账户邮箱，建立 邮箱：所有账号索引列表 的字典映射
        针对每一个账号索引，如果不在id_visited中，就在结果列表ans中填入切片好的名称列表
            并对这个索引进行dfs
        dfs对不在id_visited中的索引，遍历该索引下的所有邮箱，不在emial_visited中的加入到ans[-1]中（也就是刚填入名称列表的那一项），然后继续找同样邮箱映射的索引，继续进行dfs
        结果就是遍历ans，输出合适的格式
        '''
        # key = 邮箱 ; value = 账户编号
        belongs = collections.defaultdict(list)
        for i, j in enumerate(accounts):
            for email in j[1:]:
                belongs[email].append(i)

        emial_visited = set()
        id_visited = set()
        def dfs(id):
            if id in id_visited:
                return
            id_visited.add(id)
            # 遍历账户编号id，所对应的的所有邮箱
            for email in accounts[id][1:]:
                if email in emial_visited:
                    continue
                emial_visited.add(email)
                ans[-1].append(email)
                # dfs该邮箱的所有id，这些id中所有不重复的邮箱--都是同一个人的
                for i in belongs[email]:
                    dfs(i)
        ans = []
        for i in range(len(accounts)):
            if i not in id_visited:
                ans.append(accounts[i][:1])
                dfs(i)
        for i in range(len(ans)):
            ans[i] = ans[i][:1] + sorted(ans[i][1:])
        # print(accounts[1][0], accounts[1][:1])  # John ['John']  切片返回的是列表
        return ans

# @lc code=end

'''
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        self.parent[root_x] = root_y

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        # 有相同邮箱的名称是同一个人的，因此考虑将每个名称的邮箱合并，这样就可以形成不同人个数 个连通分量。
        # 为了编码方便，邮箱与数字编号进行字典映射，合并的是数字。创建字典email2Index = {}
        # 针对每一个邮箱，找到其根节点（index),创建字典index2Email,让每个根节点index存放对应该连通分量的所有邮箱。
        # 有了每个人的所有邮箱，要知道这个人是谁，要有一个字典email2Name = {}，根据邮箱名称找对应的人名称。
        # 邮箱是按顺序排的
        '''
        email2Index, email2Name = {}, {}
        for account in accounts:
            for email in account[1:]:
                if email not in email2Index:  # 不重复的邮箱
                    email2Index[email] = len(email2Index)
                    email2Name[email] = account[0]

        uf = UnionFind(len(email2Index))
        for account in accounts:
            emails = account[1]
            for email in account[2:]:
                uf.union(email2Index[emails], email2Index[email])
        
        index2Email = collections.defaultdict(list)
        for email, index in email2Index.items():  # 一些元组组成的列表
            index2Email[uf.find(index)].append(email)

        ans = []
        for ema in index2Email.values():
            ans.append([email2Name[ema[0]]] + sorted(ema))
        
        return ans
'''
