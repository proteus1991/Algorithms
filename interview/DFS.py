# 作者：CjwIsACaiBi
# 链接：https://www.nowcoder.com/discuss/636071?type=all&order=time&pos=&page=0&channel=-1&source_id=search_all_nctrack
# 来源：牛客网
#
# 第一行输入三个数据：m代表矩阵行数，n代表矩阵列数，t代表最长玩时间
# 接下来输入m*矩阵，矩阵元素的值为该景点需要的游玩时间。
# 要求：从左上角出发，只能向下或向右，最终到达右下角，游玩用时最接近t且不超过t
# 输出最长的游玩用时，不存在合适的用时返回-1

# 例：
# m =5, n= 5, t = 30
# [3, 5, 4, 2, 3
#  4, 5, 3, 4, 3
#  4, 3, 5, 3, 2
#  2, 5, 3, 3, 5
#  5, 3, 4, 4, 1]
# output = 30


def maxpath(matrix, limit):
    if not matrix or not matrix[0]: return -1
    costs = []
    pass_path = []

    def dfs(i, j, cost, path):
        if cost > limit:
            return
        if i >= len(matrix) or j >= len(matrix[0]):
            return
        if i == len(matrix) - 1 and j == len(matrix[0]) - 1 and cost + matrix[i][j] <= limit:
            costs.append(cost + matrix[i][j])
            pass_path.append(path + [matrix[i][j]])
            return
        dfs(i + 1, j, cost + matrix[i][j], path + [matrix[i][j]])
        dfs(i, j + 1, cost + matrix[i][j], path + [matrix[i][j]])

    dfs(0, 0, 0, [])
    ans = 0
    ans_path = []
    for id, i in enumerate(costs):
        ans = max(i, ans)
        if ans == i:
            ans_path.append(pass_path[id])
    print(costs)
    print(ans_path)
    if ans == 0:
        ans = -1
    return ans


matrix = [[3, 5, 4, 2, 3],
          [4, 5, 3, 4, 3],
          [4, 3, 5, 3, 2],
          [2, 5, 3, 3, 5],
          [5, 3, 4, 4, 1]]

# matrix = [[1, 1, 1, 1, 1],
#           [1, 1, 1, 1, 1],
#           [1, 1, 1, 1, 1],
#           [1, 1, 1, 2, 2],
#           [1, 1, 1, 2, 2]]

limit = 30

print(maxpath(matrix, limit))