# 有 N 种物品和一个容量是 V 的背包，每种物品都有无限件可用。
#
# 第 i 种物品的体积是 vi，价值是 wi。
#
# 求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
# 输出最大价值。
#
# 输入格式
# 第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。
#
# 接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 种物品的体积和价值。
#
# 输出格式
# 输出一个整数，表示最大价值。
#
# 数据范围
# 0<N,V≤1000
# 0<vi,wi≤1000
# 输入样例
# 4 5
# 1 2
# 2 4
# 3 4
# 4 5
# 输出样例：
# 10

# dp list is 2D (may exceed time, but help to understand this complete knapsack problem)
while True:
    try:
        num, weight = map(int, input().split())
        v, w = [0], [0]
        for i in range(num):
            one_v, one_w = map(int, input().split())
            v.append(one_v)
            w.append(one_w)
        dp = [[0 for _ in range(weight + 1)] for _ in range(num + 1)]
        for i in range(1, num + 1):
            for j in range(1, weight + 1):
                dp[i][j] = dp[i - 1][j]
                for k in range(1, j // v[i] + 1):
                    t = dp[i - 1][j - k * v[i]] + k * w[i]
                    if t > dp[i][j]:
                        dp[i][j] = t

        print(dp[-1][-1])

    except:
        break

# dp list is 2D (better)
while True:
    try:
        num, weight = map(int, input().split())
        v, w = [0], [0]
        for i in range(num):
            one_v, one_w = map(int, input().split())
            v.append(one_v)
            w.append(one_w)
        dp = [[0 for _ in range(weight + 1)] for _ in range(num + 1)]
        for i in range(1, num + 1):
            for j in range(1, weight + 1):
                if j >= v[i]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - v[i]] + w[i])
                else:
                    dp[i][j] = dp[i - 1][j]

        print(dp[-1][-1])

    except:
        break

# dp list is 1D
while True:
    try:
        num, weight = map(int, input().split())
        v, w = [0], [0]
        for i in range(num):
            one_v, one_w = map(int, input().split())
            v.append(one_v)
            w.append(one_w)
        dp = [0 for _ in range(weight + 1)]
        for i in range(1, num + 1):
            for j in range(1, weight + 1):
                if j - v[i] >= 0:
                    dp[j] = max(dp[j], dp[j - v[i]] + w[i])

        print(dp[-1])

    except:
        break

