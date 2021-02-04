'''
2121.2.4 lzx
AcWing 897. 最长公共子序列 题解：https://www.acwing.com/activity/content/code/content/795764/
给定两个长度分别为N和M的字符串A和B，求既是A的子序列又是B的子序列的字符串长度最长是多少。

输入格式
第一行包含两个整数N和M。
第二行包含一个长度为N的字符串，表示字符串A。
第三行包含一个长度为M的字符串，表示字符串B。
字符串均由小写字母构成。

输出格式
输出一个整数，表示最大长度。

数据范围
1≤N,M≤1000

输入样例：
4 5
acbd
abedc

输出样例：
3
'''


n, m = map(int, input().split())
a = list(input())
b = list(input())
f = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        f[i][j] = max(f[i - 1][j], f[i][j - 1])
        if a[i - 1] == b[j - 1]:
            f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1)

print(f[n][m])