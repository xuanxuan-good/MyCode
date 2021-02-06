#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 1.dp？  2.bfs  3.A*启发式搜索
        q, n = [(0, 0, 2)], len(grid)  # q表示起点，终点，走的步数
        if grid[0][0] or grid[-1][-1]:  # 左上和右下有一个被挡住，说明不存在该路径
            return -1
        elif n <= 2:
            return n
        # bfs starts
        for i, j, d in q:  # 根据q里的初始值进行不断bfs （相当于while pq:）
            # current node: i, j ; distance = d
            for x, y in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:  # 八连通
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:  # 在网格范围内 
                    if x == y == n-1:  # 且在边界上，就返回路径长度d
                        return d
                    q += [(x, y, d+1)]
                    grid[x][y] = 1  # 该点已经被遍历过，不需要再走过来
        return -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:  # A*
        n = len(grid)
        def getNeighbours(i, j):
            positions = [[-1,-1], [-1,0], [-1,1],[0,-1], [0,1], [1, -1], [1, 0], [1, 1]]
            
            for pos in positions:
                i1, j1 = i + pos[0], j + pos[1]
                
                if i1 >= 0 and i1 < n and j1 >= 0 and j1 < n and grid[i1][j1] == 0:
                    yield (i1, j1)
                    
        solution = [[999999] * n for _ in range(n)]
        solution[0][0] = 1
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        h = []
        heapq.heappush(h, (1, (0, 0, 1)))
        while h:
            est, (i, j, sp) = heapq.heappop(h)            
            solution[i][j] = sp
            if i == n - 1 and j == n - 1:
                break
            for i1, j1 in getNeighbours(i, j):
                if solution[i1][j1] > sp + 1:
                    heapq.heappush(h, (sp + 1 + max(n - i1 - 1, n - j1 - 1), (i1, j1, sp + 1)))
                    solution[i1][j1] = solution[i][j] + 1
        
        if solution[n-1][n-1] == 999999:
            return -1
        else:
            return solution[n-1][n-1]


# A* 定估价函数--曼哈顿距离 ----代码学习
from heapq import heappush, heappop

class PriorityQueue:
    
    def __init__(self, iterable=[]):
        self.heap = []
        for value in iterable:
            heappush(self.heap, (0, value))
    
    def add(self, value, priority=0):
        heappush(self.heap, (priority, value))
    
    def pop(self):
        priority, value = heappop(self.heap)
        return value
    
    def __len__(self):
        return len(self.heap)

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def reconstruct_path(came_from, start, end):
            """
            >>> came_from = {'b': 'a', 'c': 'a', 'd': 'c', 'e': 'd', 'f': 'd'}
            >>> reconstruct_path(came_from, 'a', 'e')
            ['a', 'c', 'd', 'e']
            """
            reverse_path = [end]
            while end != start:
                end = came_from[end]
                reverse_path.append(end)
            return list(reversed(reverse_path))
        
        def a_star_graph_search(
                start,
                goal_function,
                successor_function,
                heuristic
        ):
            visited = set()
            came_from = dict()
            distance = {start: 0}
            frontier = PriorityQueue()  # pq
            frontier.add(start)  # 把start放进pq
            while frontier:  # while pq
                node = frontier.pop()  # 每次把头结点取出来
                if node in visited:  # 判断重复，则进行下一次循环
                    continue
                if goal_function(node):  # 如果走到路径最后
                    return reconstruct_path(came_from, start, node)  # 把路径重新找出来？
                visited.add(node)
                for successor in successor_function(node):  # 继续搜索，开始扩散结点（八连通图）
                    frontier.add(
                        successor,
                        priority = distance[node] + 1 + heuristic(successor)
                    )  # 得到的点为successor，其优先级 通过heuristic 算出新的priority，按照优先级加入到优先队列中
                    # 优先级：当前distance+1+ successor与终点之间的距离【坐标差--比较当前坐标 与 右下角坐标的距离】
                    if (successor not in distance
                        or distance[node] + 1 < distance[successor]):
                        distance[successor] = distance[node] + 1  # distance更远（加速或者缓存）
                        came_from[successor] = node
            return None

        def get_goal_function(grid):
            """
            >>> f = get_goal_function([[0, 0], [0, 0]])
            >>> f((0, 0))
            False
            >>> f((0, 1))
            False
            >>> f((1, 1))
            True
            """
            M = len(grid)
            N = len(grid[0])
            def is_bottom_right(cell):
                return cell == (M-1, N-1)  # 判断当前点是否已经走到最后
            return is_bottom_right  # true就是走到了

        def get_successor_function(grid):
            """
            >>> f = get_successor_function([[0, 0, 0], [0, 1, 0], [1, 0, 0]])
            >>> sorted(f((1, 2)))
            [(0, 1), (0, 2), (2, 1), (2, 2)]
            >>> sorted(f((2, 1)))
            [(1, 0), (1, 2), (2, 2)]
            """
            def get_clear_adjacent_cells(cell):
                i, j = cell
                return (
                    (a, b) 
                    for a, b in[(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)] 
                    if 0 <= a < len(grid) and 0 <= b < len(grid[0]) and grid[a][b] == 0
                )
            return get_clear_adjacent_cells  # 八连通扩散，并且返回的（a, b）值要在网格内，且网格对应值是0

        def get_heuristic(grid):
            """
            >>> f = get_heuristic([[0, 0], [0, 0]])
            >>> f((0, 0))
            1
            >>> f((0, 1))
            1
            >>> f((1, 1))
            0
            """
            M, N = len(grid), len(grid[0])
            (a, b) = goal_cell = (M - 1, N - 1)
            def get_clear_path_distance_from_goal(cell):
                (i, j) = cell  # 当前点 与 右下终点 之间
                return max(abs(a - i), abs(b - j))  # 横坐标差的绝对值 与 纵坐标差 的绝对值 的最大值
            return get_clear_path_distance_from_goal
        
        # 主要函数 a_star_graph_search
        shortest_path = a_star_graph_search(
            start              = (0, 0), 
            goal_function      = get_goal_function(grid),  # 找最后目标是什么
            successor_function = get_successor_function(grid),  # 找下一个优先的来取
            heuristic          = get_heuristic(grid)  # 估价函数
        )
        if shortest_path is None or grid[0][0] == 1:
            return -1
        else:
            return len(shortest_path)
# @lc code=end

