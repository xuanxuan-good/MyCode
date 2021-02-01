'''
2020.02.01 lzx
AcWing 2. 01背包问题 题解：https://www.acwing.com/activity/content/code/content/778271/
（每件物品只能选一次）
有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。
第 i 件物品的体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。
接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤1000
0<vi,wi≤1000

输入样例
4 5
1 2
2 4
3 4
4 5
输出样例：
8
'''


# 经典01背包问题 1207ms
n, m = map(int, input().split())
v, w = [0] * (n + 1), [0] * (n + 1)
f = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    v[i], w[i] = map(int, input().split())

for i in range(1, n + 1):
    for j in range(m + 1):
        f[i][j] = f[i - 1][j]
        if j >= v[i]:
            f[i][j] = max(f[i][j], f[i - 1][j - v[i]] + w[i])

print(f[n][m])



# 01背包问题优化 1086ms
n, m = map(int, input().split())
v, w = [0] * (n + 1), [0] * (n + 1)
f = [0] * (m + 1)

for i in range(1, n + 1):
    v[i], w[i] = map(int, input().split())

for i in range(1, n + 1):
    for j in range(m, v[i] - 1, -1):
        f[j] = max(f[j], f[j - v[i]] + w[i])

print(f[m])