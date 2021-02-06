#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#

# @lc code=start
# 方向变换向量。 类似四连通图，八连通图，2*3板子---对应的交换坐标（一维字符数组里的下标）
# 0 1 2
# 3 4 5
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4],
    4: [1, 3, 5],
    5: [2, 4]
}  # 表示的是 位置
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 也叫 8puzzle   1.dfs  2.bfs-更快找到最优解  3.A*
        # bfs 1
        visited = set()
        cnt = 0
        s = "".join(str(c) for row in board for c in row)  # 2*3换成一维字符串

        q = [s]  # 起点为s，board的初始状态  e.g. 123405,不断用0和其他字符进行交换，看怎么能变成123450
        while q:
            new = []  # 下次新的要扩散的节点
            for s in q:  # 从q里把所有的s取出来，依次处理
                visited.add(s)
                if s == "123450":
                    return cnt  # 最终目标状态
                arr = [c for c in s]  # s进一步扩散，先组成一个字符数组

                # 开始移动0
                zero_index = s.index("0")  # 找到0的位置  因为只能对0进行操作
                for move in moves[zero_index]:
                    new_arr = arr[:]  # 重新拷贝一份
                    new_arr[zero_index], new_arr[move] = new_arr[move], new_arr[zero_index]  # 零和可移动字符的位置 进行交换
                    new_s = "".join(new_arr)
                    if new_s not in visited:
                        new.append(new_s)
            cnt += 1  # 变换步数
            q = new
        return -1

        '''
        # bfs 2
        board = board[0] + board[1]
        moves = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]
        q, visited = [(tuple(board), board.index(0), 0)], set()  # tuple是为了加速？可以直接相等比较
        while q:
            state, now, step = q.pop(0)
            if state == (1, 2, 3, 4, 5, 0):
                return step
            for next in moves[now]:
                new_state = list(state)  #
                new_state[next], new_state[now] = new_state[now], new_state[next]
                new_state = tuple(new_state)
                if new_state not in visited:
                    q.append((new_state, next, step+1))
            visited.add(state)
        return -1
        '''

# @lc code=end

