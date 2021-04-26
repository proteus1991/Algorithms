#   B---D
#  /|  /|\
# A | / | F
#  \|/  |
#   C---E

graph = {'A': ['B', 'C'],
         'B': ['A', 'C', 'D'],
         'C': ['A', 'B', 'D', 'E'],
         'D': ['B', 'C', 'E', 'F'],
         'E': ['C', 'D'],
         'F': ['D']}

# depth-first Search (BFS)
# 一条路走到黑

# use stack rather than recursion
def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while stack:
        node = stack.pop()
        ad_nodes = graph[node]     # find its adjacent nodes
        for i in ad_nodes:
            if i not in seen:
                stack.append(i)
                seen.add(i)
        print(node)


def dfs_recursion(graph, s):
    seen = set()

    def dfs(seen, graph, s):
        print(s)
        seen.add(s)
        ad_nodes = graph[s]
        for i in ad_nodes:
            if i not in seen:
                dfs(seen, graph, i)

    dfs(seen, graph, s)


print('not recursion')
DFS(graph, 'A')

print('recursion')
dfs_recursion(graph, 'F')
