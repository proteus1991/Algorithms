# [[4, 5], [1, 2], [2, 4], [3, 4], [4, 5]]

# dp list is 2D
while True:
    try:
        num, weight = map(int, input().split())
        w, v = [0], [0]
        for i in range(num):
            one_w, one_v = map(int, input().split())
            w.append(one_w)
            v.append(one_v)
        dp = [[0 for _ in range(weight + 1)] for _ in range(num + 1)]
        for i in range(1, num + 1):
            for j in range(1, weight + 1):
                if j - w[i] >= 0:
                    dp[i][j] = max(dp[i-1][j], dp[i - 1][j - w[i]] + v[i])
                else:
                    dp[i][j] = dp[i-1][j]

        print(dp[-1][-1])

    except:
        break

# dp list is 1D
while True:
    try:
        num, weight = map(int, input().split())
        w, v = [0], [0]
        for i in range(num):
            one_w, one_v = map(int, input().split())
            w.append(one_w)
            v.append(one_v)
        dp = [0 for _ in range(weight + 1)]
        for i in range(1, num + 1):
            for j in range(weight, 0, -1):  # reverse order, for j in range(weight, w[i]-1, -1)
                if j - w[i] >= 0:
                    dp[j] = max(dp[j], dp[j - w[i]] + v[i])

        print(dp[-1])

    except:
        break
