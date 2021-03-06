'''
2021.2.4 lzx 
AcWing 902. 最短编辑距离 题解：https://www.acwing.com/activity/content/code/content/799335/
给定两个字符串A和B，现在要将A经过若干操作变为B，可进行的操作有：
    删除–将字符串A中的某个字符删除。
    插入–在字符串A的某个位置插入某个字符。
    替换–将字符串A中的某个字符替换为另一个字符。
现在请你求出，将A变为B至少需要进行多少次操作。

输入格式
第一行包含整数n，表示字符串A的长度第二行包含一个长度为n的字符串A。
第三行包含整数m，表示字符串B的长度。第四行包含一个长度为m的字符串B。
字符串中均只包含大写字母。

输出格式
输出一个整数，表示最少操作次数。

数据范围
1≤n,m≤1000

输入样例：
10 
AGTCTGACGC
11 
AGTAAGTAGGC

输出样例：
4
'''


n = int(input())
a = list(input())
m = int(input())
b = list(input())

f = [[0] * (m + 1) for _ in range(n +1)]

for i in range(n + 1): f[i][0] = i
for j in range(m + 1): f[0][j] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        f[i][j] = min(f[i - 1][j] + 1, f[i][j - 1] + 1)
        f[i][j] = min(f[i][j], f[i - 1][j - 1] + (a[i - 1] != b[j - 1]))

print(f[n][m])