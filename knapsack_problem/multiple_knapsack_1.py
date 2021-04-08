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
# 0<N,V≤100
# 0<vi,wi,si≤100
# 输入样例
# 4 5
# 1 2 3
# 2 4 1
# 3 4 3
# 4 5 2
# 输出样例：
# 10


# 2D
while True:
    try:
        num, weight = map(int, input().split())
        v, w, s = [0], [0], [0]
        for i in range(num):
            one_v, one_w, one_s = map(int, input().split())
            v.append(one_v)
            w.append(one_w)
            s.append(one_s)
        dp = [[0 for _ in range(weight + 1)] for _ in range(num + 1)]
        for i in range(1, num + 1):
            for j in range(1, weight + 1):
                dp[i][j] = dp[i - 1][j]     # if 1D, no need for this step
                count = min(s[i], j // v[i])
                for k in range(1, count + 1):
                    t = dp[i - 1][j - k * v[i]] + k * w[i]
                    if t > dp[i][j]:
                        dp[i][j] = t

        print(dp[-1][-1])

    except:
        break


# 1D
while True:
    try:
        num, weight = map(int, input().split())
        v, w, s = [0], [0], [0]

        for i in range(num):
            one_v, one_w, one_s = map(int, input().split())
            v.append(one_v)
            w.append(one_w)
            s.append(one_s)
        dp = [0 for _ in range(weight + 1)]
        for i in range(1, num + 1):
            for j in range(weight, 0, -1):
                count = min(s[i], j//v[i])
                for k in range(1, count + 1):
                    dp[j] = max(dp[j], dp[j - k*v[i]] + k*w[i])

        print(dp[-1])

    except:
        break
