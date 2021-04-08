# 有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。
#
# 第 i 件物品的体积是 vi，价值是 wi。
#
# 求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
# 输出最大价值。
#
# 输入格式
# 第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。
#
# 接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。
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
# 8

# dp list is 2D
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
                if j - v[i] >= 0:
                    dp[i][j] = max(dp[i-1][j], dp[i - 1][j - v[i]] + w[i])
                else:
                    dp[i][j] = dp[i-1][j]

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
            for j in range(weight, 0, -1):  # reverse order, for j in range(weight, w[i]-1, -1)
                if j - v[i] >= 0:
                    dp[j] = max(dp[j], dp[j - v[i]] + w[i])

        print(dp[-1])

    except:
        break
