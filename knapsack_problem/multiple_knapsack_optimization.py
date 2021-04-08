# 有 N 种物品和一个容量是 V 的背包。
#
# 第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。
#
# 求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
# 输出最大价值。
#
# 输入格式
# 第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。
#
# 接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。
#
# 输出格式
# 输出一个整数，表示最大价值。
#
# 数据范围
# 0<N≤1000
# 0<V≤2000
# 0<vi,wi,si≤2000
# 提示：
# 本题考查多重背包的二进制优化方法。
#
# 输入样例
# 4 5
# 1 2 3
# 2 4 1
# 3 4 3
# 4 5 2
# 输出样例：
# 10

# optimization
# change to 0-1 knapsack problem
# https://www.acwing.com/problem/content/5/
while True:
    try:
        num, weight = map(int, input().split())
        v, w = [0], [0]
        for i in range(num):
            one_v, one_w, one_s = map(int, input().split())

            temp = 1
            while temp <= one_s:
                v.append(temp * one_v)
                w.append(temp * one_w)
                one_s -= temp
                temp *= 2
            if one_s > 0:
                v.append(one_s * one_v)
                w.append(one_s * one_w)

        dp = [0 for _ in range(weight + 1)]
        for i in range(1, len(v)):
            for j in range(weight, 0, -1):
                if j - v[i] >= 0:
                    dp[j] = max(dp[j], dp[j - v[i]] + w[i])

        print(dp[-1])

    except:
        break