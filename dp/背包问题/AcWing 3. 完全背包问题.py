'''
2020.02.01 lzx
AcWing 3. 完全背包问题题解：https://www.acwing.com/activity/content/code/content/778610/
（每件物品可以选无限次）
有 N 种物品和一个容量是 V 的背包，每种物品都有无限件可用。
第 i 种物品的体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。
接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 种物品的体积和价值。

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
10
'''


# 完全背包 O(n * m^2), 10^9, 会超时
n, m = map(int, input().split())
v, w = [0] * (n + 1), [0] * (n + 1)
f = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    v[i], w[i] = map(int, input().split())

for i in range(1, n + 1):
    for j in range(m + 1):
        k = 0
        while j >= k * v[i]:
            f[i][j] = max(f[i][j], f[i - 1][j - v[i] * k] + w[i] * k)
            k += 1

print(f[n][m])



# 完全背包优化1 1203ms
n, m = map(int, input().split())
v, w = [0] * (n + 1), [0] * (n + 1)
f = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    v[i], w[i] = map(int, input().split())

for i in range(1, n + 1):
    for j in range(m + 1):
        f[i][j] = f[i - 1][j]
        if j >= v[i]:
            f[i][j] = max(f[i][j], f[i][j - v[i]] + w[i])

print(f[n][m])



# 完全背包优化2 1193ms
n, m = map(int, input().split())
v, w = [0] * (n + 1), [0] * (n + 1)
f = [0] * (m + 1)

for i in range(1, n + 1):
    v[i], w[i] = map(int, input().split())

for i in range(1, n + 1):
    for j in range(v[i], m + 1):
        f[j] = max(f[j], f[j - v[i]] + w[i])

print(f[m])