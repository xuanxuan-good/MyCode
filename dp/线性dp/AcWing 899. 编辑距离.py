'''
2021.2.4 lzx 
AcWing 899. 编辑距离 题解：https://www.acwing.com/activity/content/code/content/799957/
给定n个长度不超过10的字符串以及m次询问，每次询问给出一个字符串和一个操作次数上限。
对于每次询问，请你求出给定的n个字符串中有多少个字符串可以在上限操作次数内经过操作变成询问给出的字符串。
每个对字符串进行的单个字符的插入、删除或替换算作一次操作。

输入格式
第一行包含两个整数n和m。
接下来n行，每行包含一个字符串，表示给定的字符串。
再接下来m行，每行包含一个字符串和一个整数，表示一次询问。
字符串中只包含小写字母，且长度均不超过10。

输出格式
输出共m行，每行输出一个整数作为结果，表示一次询问中满足条件的字符串个数。

数据范围
1≤n,m≤1000,

输入样例：
3 2
abc
acd
bcd
ab 1
acbd 2

输出样例：
1
3
'''


def edit_distance(a, b):
    la, lb = len(a), len(b)
    f = [[0] * (lb + 1) for _ in range(la + 1)]

    for i in range(la + 1): f[i][0] = i
    for j in range(lb + 1): f[0][j] = j

    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            f[i][j] = min(f[i - 1][j] + 1, f[i][j - 1] + 1)
            f[i][j] = min(f[i][j], f[i - 1][j - 1] + (a[i - 1] != b[j - 1]))

    return f[la][lb]


if __name__ == '__main__':
    n, m = map(int, input().split())
    strs = []
    for _ in range(n):
        strs.append(list(input()))

    for _ in range(m):
        s, limit = input().split()
        ls, limit = list(s), int(limit)
        res = 0

        for i in range(n):
            if edit_distance(strs[i], ls) <= limit:
                res += 1

        print(res)