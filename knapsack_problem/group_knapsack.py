# 有 N 组物品和一个容量是 V 的背包。
#
# 每组物品有若干个，同一组内的物品最多只能选一个。
# 每件物品的体积是 vij，价值是 wij，其中 i 是组号，j 是组内编号。
#
# 求解将哪些物品装入背包，可使物品总体积不超过背包容量，且总价值最大。
#
# 输出最大价值。
#
# 输入格式
# 第一行有两个整数 N，V，用空格隔开，分别表示物品组数和背包容量。
#
# 接下来有 N 组数据：
#
# 每组数据第一行有一个整数 Si，表示第 i 个物品组的物品数量；
# 每组数据接下来有 Si 行，每行有两个整数 vij,wij，用空格隔开，分别表示第 i 个物品组的第 j 个物品的体积和价值；
# 输出格式
# 输出一个整数，表示最大价值。
#
# 数据范围
# 0<N,V≤100
# 0<Si≤100
# 0<vij,wij≤100
# 输入样例
# 3 5
# 2
# 1 2
# 2 4
# 1
# 3 4
# 1
# 4 5
# 输出样例：
# 8

while True:
    try:
        num, weight = map(int, input().split())
        v = [[0] for _ in range(num + 1)]
        w = [[0] for _ in range(num + 1)]
        for i in range(1, num + 1):
            group_num = int(input())
            for j in range(1, group_num + 1):
                one_v, one_w = map(int, input().split())
                v[i].append(one_v)
                w[i].append(one_w)

        dp = [0 for _ in range(weight + 1)]

        for i in range(1, num + 1):
            for j in range(weight, 0, -1):
                temp_max = dp[j]
                for k in range(len(v[i])):
                    if j >= v[i][k] and dp[j-v[i][k]] + w[i][k] > temp_max:
                        temp_max = dp[j-v[i][k]] + w[i][k]

                dp[j] = temp_max

        print(dp[-1])

    except:
        break

