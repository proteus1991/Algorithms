# 题目描述：
# 幼儿园老师安排小朋友做游戏，现在需要给N个小朋友进行分组，老师让每个同学写一个名字，代表这位小朋友想和谁分到一组，请问老师在满足所有小朋友意思的情况下，最多可以将班级分为几组？
#
# 输入描述：
# 第一行输入N，0 < N <= 100000
# 接下来是N行代表每个小朋友希望和谁分到一组，如:”John
# Jack”, 代表John希望和Jack分到一组，两个名字之间以空格分割，名字本身不存在空格。
#
# 输出描述：
# 分组的最多数量
#
# 输入：
# 6
# Jack Tom
# Alice John
# Jessica Leonie
# Tom Alice
# John Jack
# Leonie Jessica
#
# 输出：
# 2

def find(x, parent):
    r = x
    while parent[r] != r:
        r = parent[r]
    return r


def union(x, y, parent):
    x_root = find(x, parent)
    y_root = find(y, parent)
    if x_root != y_root:
        parent[y_root] = x_root


while True:
    try:
        num = int(input())
        adict, parent = {}, {}
        out = set()
        for i in range(num):
            key, value = input().split()
            adict[key] = value
            parent[key] = key

        for x, y in adict.items():
            union(x, y, parent)

        for i in parent:
            out.add(find(i, parent))

        print(len(out))
    except:
        break

