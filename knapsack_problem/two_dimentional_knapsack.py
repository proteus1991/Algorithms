# 有 N 件物品和一个容量是 V 的背包，背包能承受的最大重量是 M。
#
# 每件物品只能用一次。体积是 vi，重量是 mi，价值是 wi。
#
# 求解将哪些物品装入背包，可使物品总体积不超过背包容量，总重量不超过背包可承受的最大重量，且价值总和最大。
# 输出最大价值。
#
# 输入格式
# 第一行两个整数，N，V,M，用空格隔开，分别表示物品件数、背包容积和背包可承受的最大重量。
#
# 接下来有 N 行，每行三个整数 vi,mi,wi，用空格隔开，分别表示第 i 件物品的体积、重量和价值。
#
# 输出格式
# 输出一个整数，表示最大价值。
#
# 数据范围
# 0<N≤1000
# 0<V,M≤100
# 0<vi,mi≤100
# 0<wi≤1000
# 输入样例
# 4 5 6
# 1 2 3
# 2 4 4
# 3 4 5
# 4 5 6
# 输出样例：
# 8

while True:
    try:
        N, V, M = map(int, input().split())
        v, m, w = [0], [0], [0]
        for i in range(N):
            one_v, one_m, one_w = map(int, input().split())
            v.append(one_v)
            m.append(one_m)
            w.append(one_w)

        dp = [[0 for _ in range(M + 1)] for _ in range(V + 1)]

        for i in range(1, N + 1):
            for j in range(V, 0, -1):
                for k in range(M, 0, -1):
                    if j - v[i] >= 0 and k - m[i] >= 0:
                        dp[j][k] = max(dp[j][k], dp[j-v[i]][k-m[i]] + w[i])

        print(dp[-1][-1])

    except:
        break

