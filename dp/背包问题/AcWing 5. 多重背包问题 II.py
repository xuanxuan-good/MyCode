'''
2020.02.01 lzx
AcWing 5. 多重背包问题 II 题解：https://www.acwing.com/activity/content/code/content/779465/
（每件物品只能选s[i]次，但是数据量变大了）
有 N 种物品和一个容量是 V 的背包。
第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。
接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N≤1000
0<V≤2000
0<vi,wi,si≤2000
提示：
本题考查多重背包的二进制优化方法。

输入样例
4 5
1 2 3
2 4 1
3 4 3
4 5 2
输出样例：
10
'''


# 多重背包问题的二进制优化, O(n m logs) ---> 2 * 10^7
n, m = map(int, input().split())
M = 2010
v, w = [0], [0]
f = [0] * (m + 1)

for i in range(n):
    # 体积，价值，数量
    a, b, s = map(int, input().split())
    k = 1
    while k <= s:
        v.append(k * a)
        w.append(k * b)
        s -= k
        k *= 2
    if s > 0:
        v.append(s * a)
        w.append(s * b)
        s -= 1

cnt = len(v)
for i in range(1, cnt):
    for j in range(m, v[i] - 1, -1):
        f[j] = max(f[j], f[j - v[i]] + w[i])

print(f[m])