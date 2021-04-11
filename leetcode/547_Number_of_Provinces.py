from typing import List


class Solution:
    def find(self, x, parent):
        r = x  # r means the root
        while parent[r] != r:
            r = parent[r]
        return r

    # optimization based on rank. There is another way based on size.
    def union(self, x, y, parent, rank):
        x_root = self.find(x, parent)
        y_root = self.find(y, parent)

        if x_root != y_root:
            if rank[x] < rank[y]:
                parent[y_root] = x_root
            elif rank[x] < rank[y]:
                parent[x_root] = y_root
            else:
                parent[y_root] = x_root  # can add x tree to y tree as well
                rank[x_root] += 1

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        parent = []
        rank = []
        out = set()
        for i in range(len(isConnected)):
            parent.append(i)
            rank.append(0)
        for i in range(len(isConnected)):
            for j in range(i, len(isConnected[0])):
                if isConnected[i][j] == 1:
                    self.union(i, j, parent, rank)

        for i in parent:
            out.add(self.find(i, parent))

        return len(out)


if __name__ == '__main__':
    a = Solution()
    isConnected = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    print(a.findCircleNum(isConnected))
