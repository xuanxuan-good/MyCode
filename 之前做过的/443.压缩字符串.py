#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
# 给定一组字符，使用原地算法将其压缩。
# 压缩后的长度必须始终小于或等于原数组长度。
# 数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。
# 在完成原地修改输入数组后，返回数组的新长度。

# 进阶：
# 你能否仅使用O(1) 空间解决问题？

# 示例 1：
# 输入：
# ["a","a","b","b","c","c","c"]
# 输出：
# 返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
# 说明：
# "aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。

# 示例 2：
# 输入：
# ["a"]
# 输出：
# 返回 1 ，输入数组的前 1 个字符应该是：["a"]
# 解释：
# 没有任何字符串被替代。

# 示例 3：
# 输入：
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# 输出：
# 返回 4 ，输入数组的前4个字符应该是：["a","b","1","2"]。
# 解释：
# 由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
# 注意每个数字在数组中都有它自己的位置。
 

# 提示：
# 所有字符都有一个ASCII值在[35, 126]区间内。
# 1 <= len(chars) <= 1000。


# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        # write表示写入的索引；anchor表示不同字符开始读的位置
        anchor = write = 0
        for read, c in enumerate(chars):
            # 如果到最后一个字符了，或者后一个字符与当前字符不相等：此时可以原地放到输入数组中了
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = c
                write += 1
                # 如果读到的相同字符所在位置 在该字符所在第一个位置 后边。说明长度大于一
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                # 新的字符所在位置更新
                anchor = read + 1
        return write
# @lc code=end

